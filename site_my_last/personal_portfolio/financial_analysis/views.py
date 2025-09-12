from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import FinancialDocumentForm
from .models import FinancialDocument, FinancialRatio
import pdfplumber
import re


@login_required
def upload_document(request):
    """Загрузка финансового документа"""
    if request.method == 'POST':
        form = FinancialDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()

            # Анализируем PDF и рассчитываем коэффициенты
            analyze_document(document)

            return redirect('financial_results', document_id=document.id)
    else:
        form = FinancialDocumentForm()

    return render(request, 'financial_analysis/upload.html', {'form': form})


@login_required
def financial_results(request, document_id):
    """Показывает результаты финансового анализа"""
    try:
        # Используем get_object_or_404 для безопасности
        document = get_object_or_404(FinancialDocument, id=document_id, user=request.user)
        ratios = FinancialRatio.objects.filter(document=document)

        return render(request, 'financial_analysis/results.html', {
            'document': document,
            'ratios': ratios
        })

    except Exception as e:
        # Общий обработчик ошибок
        raise Http404(f"Ошибка при загрузке документа: {e}")


@login_required
def document_list(request):
    """Список всех документов пользователя"""
    documents = FinancialDocument.objects.filter(user=request.user).order_by('-upload_date')
    return render(request, 'financial_analysis/list.html', {'documents': documents})


@login_required
def debug_document(request, document_id):
    """Страница отладки для анализа текста PDF"""
    document = get_object_or_404(FinancialDocument, id=document_id, user=request.user)

    text = ""
    try:
        with pdfplumber.open(document.pdf_file.path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        text = f"Ошибка чтения PDF: {e}"

    return render(request, 'financial_analysis/debug.html', {
        'document': document,
        'pdf_text': text[:5000]  # Первые 5000 символов
    })


def analyze_document(document):
    """Анализ финансового документа и расчет коэффициентов"""
    ratios = []

    try:
        with pdfplumber.open(document.pdf_file.path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"

            print("=" * 50)
            print("ДЕБАГ: Текст из PDF")
            print("=" * 50)
            print(text[:2000])  # Первые 2000 символов для анализа
            print("=" * 50)

            # Сохраняем текст для отладки
            with open('debug_pdf_text.txt', 'w', encoding='utf-8') as f:
                f.write(text)

            # АВТОМАТИЧЕСКОЕ ОПРЕДЕЛЕНИЕ ФОРМАТА
            if "Бухгалтерский баланс" in text or "БАЛАНС" in text:
                document.document_type = 'balance'
                ratios = analyze_balance_sheet(text)
            elif "Отчет о финансовых результатах" in text or "Отчет о прибылях" in text:
                document.document_type = 'profit_loss'
                ratios = analyze_profit_loss_statement(text)
            else:
                # Пытаемся автоматически определить по характерным строкам
                ratios = auto_detect_financial_data(text)

            document.save()

    except Exception as e:
        print(f"Ошибка анализа документа: {e}")
        import traceback
        traceback.print_exc()

    # Сохраняем коэффициенты в базу
    for ratio_name, ratio_value in ratios:
        FinancialRatio.objects.create(
            document=document,
            ratio_name=ratio_name,
            ratio_value=ratio_value
        )


def analyze_balance_sheet(text):
    """Анализ бухгалтерского баланса"""
    ratios = []

    # Ищем основные показатели по разным шаблонам
    patterns = [
        # Активы
        ('Актив.*?Итого.*?([\d\s,]+)', 'total_assets'),
        ('Внеоборотные активы.*?Итого.*?([\d\s,]+)', 'non_current_assets'),
        ('Оборотные активы.*?Итого.*?([\d\s,]+)', 'current_assets'),
        ('Денежные средства.*?([\d\s,]+)', 'cash'),
        ('Запасы.*?([\d\s,]+)', 'inventory'),
        ('Дебиторская задолженность.*?([\d\s,]+)', 'receivables'),

        # Пассивы
        ('Пассив.*?Итого.*?([\d\s,]+)', 'total_liabilities'),
        ('Капитал.*?Итого.*?([\d\s,]+)', 'equity'),
        ('Уставный капитал.*?([\d\s,]+)', 'share_capital'),
        ('Нераспределенная прибыль.*?([\d\s,]+)', 'retained_earnings'),
        ('Долгосрочные.*?Итого.*?([\d\s,]+)', 'long_term_debt'),
        ('Краткосрочные.*?Итого.*?([\d\s,]+)', 'short_term_debt'),
        ('Кредиторская задолженность.*?([\d\s,]+)', 'payables'),

        # Поиск по кодам строк (стандартные коды баланса)
        ('1600.*?([\d\s,]+)', 'total_assets_code'),
        ('1700.*?([\d\s,]+)', 'total_liabilities_code'),
        ('1300.*?([\d\s,]+)', 'equity_code'),
        ('1200.*?([\d\s,]+)', 'current_assets_code'),
        ('1500.*?([\d\s,]+)', 'short_term_debt_code'),
    ]

    values = {}
    for pattern, key in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            value_str = match.group(1).replace(' ', '').replace(',', '.')
            try:
                values[key] = float(value_str)
                print(f"Найдено: {key} = {values[key]}")
            except ValueError:
                print(f"Ошибка преобразования для {key}: {value_str}")
                pass

    # Приоритет: значения по кодам, затем по названиям
    total_assets = values.get('total_assets_code') or values.get('total_assets')
    equity = values.get('equity_code') or values.get('equity')
    current_assets = values.get('current_assets_code') or values.get('current_assets')
    short_term_debt = values.get('short_term_debt_code') or values.get('short_term_debt')

    # 2. Рассчитываем коэффициенты
    if current_assets and short_term_debt:
        current_ratio = current_assets / short_term_debt
        ratios.append(('Коэффициент текущей ликвидности', round(current_ratio, 2)))
        print(f"Рассчитан коэффициент текущей ликвидности: {current_ratio}")

    if equity and total_assets:
        autonomy_ratio = equity / total_assets
        ratios.append(('Коэффициент автономии', round(autonomy_ratio, 2)))
        print(f"Рассчитан коэффициент автономии: {autonomy_ratio}")

    if values.get('cash') and short_term_debt:
        cash_ratio = values['cash'] / short_term_debt
        ratios.append(('Коэффициент абсолютной ликвидности', round(cash_ratio, 2)))

    if values.get('inventory') and current_assets:
        inventory_ratio = values['inventory'] / current_assets
        ratios.append(('Доля запасов в оборотных активах', round(inventory_ratio, 2)))

    return ratios


def analyze_profit_loss_statement(text):
    """Анализ отчета о финансовых результатах"""
    ratios = []

    patterns = [
        # Основные показатели отчета о прибылях
        ('Выручка.*?([\d\s,]+)', 'revenue'),
        ('Себестоимость.*?([\d\s,]+)', 'cost'),
        ('Валовая прибыль.*?([\d\s,]+)', 'gross_profit'),
        ('Прибыль от продаж.*?([\d\s,]+)', 'operating_profit'),
        ('Прибыль до налогообложения.*?([\d\s,]+)', 'profit_before_tax'),
        ('Чистая прибыль.*?([\d\s,]+)', 'net_profit'),
        ('Налог на прибыль.*?([\d\s,]+)', 'income_tax'),

        # Поиск по кодам строк (стандартные коды отчета)
        ('2110.*?([\d\s,]+)', 'revenue_code'),
        ('2120.*?([\d\s,]+)', 'cost_code'),
        ('2100.*?([\d\s,]+)', 'gross_profit_code'),
        ('2200.*?([\d\s,]+)', 'operating_profit_code'),
        ('2300.*?([\d\s,]+)', 'profit_before_tax_code'),
        ('2400.*?([\d\s,]+)', 'net_profit_code'),
    ]

    values = {}
    for pattern, key in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            value_str = match.group(1).replace(' ', '').replace(',', '.')
            try:
                values[key] = float(value_str)
                print(f"Найдено: {key} = {values[key]}")
            except ValueError:
                print(f"Ошибка преобразования для {key}: {value_str}")
                pass

    # Приоритет: значения по кодам, затем по названиям
    revenue = values.get('revenue_code') or values.get('revenue')
    net_profit = values.get('net_profit_code') or values.get('net_profit')
    gross_profit = values.get('gross_profit_code') or values.get('gross_profit')
    operating_profit = values.get('operating_profit_code') or values.get('operating_profit')

    # Расчет коэффициентов
    if revenue and net_profit:
        profitability = (net_profit / revenue) * 100
        ratios.append(('Рентабельность продаж (%)', round(profitability, 2)))
        print(f"Рассчитана рентабельность продаж: {profitability}%")

    if revenue and gross_profit:
        gross_margin = (gross_profit / revenue) * 100
        ratios.append(('Маржа валовой прибыли (%)', round(gross_margin, 2)))

    if revenue and operating_profit:
        operating_margin = (operating_profit / revenue) * 100
        ratios.append(('Рентабельность операционной деятельности (%)', round(operating_margin, 2)))

    return ratios


def auto_detect_financial_data(text):
    """Автоматическое определение финансовых данных"""
    ratios = []

    print("Автопоиск финансовых данных...")

    # Простой поиск чисел рядом с ключевыми словами
    financial_terms = [
        'Выручка', 'Прибыль', 'Актив', 'Пассив', 'Капитал',
        'Оборотные', 'Внеоборотные', 'Обязательства', 'Доход',
        'Расход', 'Затраты', 'Налог', 'Дивиденды'
    ]

    for term in financial_terms:
        pattern = f"{term}.*?([\d\s,]+)"
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            value_str = match.replace(' ', '').replace(',', '.')
            try:
                value = float(value_str)
                print(f"Автонайдено: {term} = {value}")
            except ValueError:
                pass

    return ratios


def extract_balance_value(text, section_name, total_name, code):
    """Извлекает значение из баланса по коду строки"""
    # Сначала ищем по коду строки
    code_pattern = f"{code}\\s*[\\d\\s,]+\\s*([\\d\\s,]+)"
    match = re.search(code_pattern, text)
    if match:
        value_str = match.group(1).replace(' ', '').replace(',', '.')
        try:
            return float(value_str)
        except ValueError:
            pass

    # Если не нашли по коду, ищем по названию раздела
    name_pattern = f"{section_name}.*?{total_name}.*?([\\d\\s,]+)"
    match = re.search(name_pattern, text, re.IGNORECASE | re.DOTALL)
    if match:
        value_str = match.group(1).replace(' ', '').replace(',', '.')
        try:
            return float(value_str)
        except ValueError:
            return None
    return None


def extract_profit_value(text, line_name, code):
    """Извлекает значение из отчета о финансовых результатах"""
    # Сначала ищем по коду
    code_pattern = f"{code}\\s*[\\d\\s,]+\\s*([\\d\\s,]+)"
    match = re.search(code_pattern, text)
    if match:
        value_str = match.group(1).replace(' ', '').replace(',', '.')
        try:
            return float(value_str)
        except ValueError:
            pass

    # Затем ищем по названию строки
    name_pattern = f"{line_name}.*?([\\d\\s,]+)"
    match = re.search(name_pattern, text, re.IGNORECASE | re.DOTALL)
    if match:
        value_str = match.group(1).replace(' ', '').replace(',', '.')
        try:
            return float(value_str)
        except ValueError:
            return None
    return None