from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
from .forms import FinancialDocumentForm
from .models import FinancialDocument, FinancialRatio
import pdfplumber
import re
from typing import List, Tuple
import logging

logger = logging.getLogger(__name__)


@login_required
def upload_document(request):
    """Загрузка финансового документа"""
    if request.method == 'POST':
        form = FinancialDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                document = form.save(commit=False)
                document.user = request.user
                document.save()

                # Анализируем документ
                analyze_document(document)

                messages.success(request, 'Документ успешно загружен и проанализирован!')
                return redirect('financial_results', document_id=document.id)

            except Exception as e:
                messages.error(request, f'Ошибка при обработке документа: {str(e)}')
                return render(request, 'financial_analysis/upload.html', {'form': form})
    else:
        form = FinancialDocumentForm()

    return render(request, 'financial_analysis/upload.html', {'form': form})


@login_required
def financial_analysis_page(request):
    """Главная страница финансового анализа"""
    recent_docs = FinancialDocument.objects.filter(user=request.user).order_by('-upload_date')[:3]
    return render(request, 'financial_analysis/financial_analysis.html', {
        'recent_docs': recent_docs
    })


@login_required
def financial_results(request, document_id):
    """Показывает результаты финансового анализа"""
    document = get_object_or_404(FinancialDocument, id=document_id, user=request.user)
    ratios = FinancialRatio.objects.filter(document=document)
    return render(request, 'financial_analysis/results.html', {
        'document': document,
        'ratios': ratios
    })


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
        'pdf_text': text[:5000]
    })


def analyze_document(document):
    """Анализ финансового документа и расчет коэффициентов"""
    try:
        with pdfplumber.open(document.pdf_file.path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"

            # Определяем тип документа
            if re.search(r'Отчет о финансовых результатах|прибылях и убытках|2110.*2120|Выручка|Себестоимость', text,
                         re.IGNORECASE):
                document.document_type = 'profit_loss'
                ratios = analyze_profit_loss_statement(text)
            elif re.search(r'Отчет о движении денежных средств|ОДДС|денежные потоки|4100|4200|4300', text,
                           re.IGNORECASE):
                document.document_type = 'cash_flow'
                ratios = analyze_cash_flow_statement(text)
            elif re.search(r'Бухгалтерский баланс|АКТИВ|ПАССИВ|1600|1700|1300', text, re.IGNORECASE):
                document.document_type = 'balance'
                ratios = analyze_balance_sheet(text)
            else:
                ratios = auto_detect_financial_data(text)
                document.document_type = 'auto_detected' if ratios else 'unknown'

            document.save()

            # Сохраняем коэффициенты в базу - гарантируем float
            for ratio_name, ratio_value in ratios:
                # Преобразуем значение в float
                try:
                    numeric_value = float(ratio_value)
                except (ValueError, TypeError):
                    numeric_value = 0.0

                FinancialRatio.objects.create(
                    document=document,
                    ratio_name=str(ratio_name),
                    ratio_value=numeric_value
                )

    except Exception as e:
        logger.error(f"Ошибка анализа документа: {e}")
        # Создаем запись об ошибке
        FinancialRatio.objects.create(
            document=document,
            ratio_name='Ошибка анализа',
            ratio_value=0.0
        )


def safe_float_conversion(value):
    """Безопасное преобразование в float"""
    try:
        if isinstance(value, (int, float)):
            return float(value)
        elif isinstance(value, str):
            # Очищаем строку от пробелов и нечисловых символов
            cleaned = re.sub(r'[^\d\.\-]', '', value.replace(',', '.').replace(' ', ''))
            if cleaned and cleaned != '-':
                return float(cleaned)
        return 0.0
    except (ValueError, TypeError):
        return 0.0


def parse_financial_value(value_str: str) -> float:
    """Парсит финансовое значение из строки с учетом российского формата"""
    try:
        cleaned_str = value_str.strip()
        if cleaned_str in ['', '-', '—', '–', 'н/д', 'Н/Д']:
            return 0.0

        # Обработка отрицательных чисел в скобках
        is_negative = cleaned_str.startswith('(') and cleaned_str.endswith(')')

        # Удаляем все нечисловые символы кроме цифр и точки
        numeric_str = re.sub(r'[^\d]', '', cleaned_str)

        if not numeric_str:
            return 0.0

        value = float(numeric_str)
        return -value if is_negative else value

    except (ValueError, TypeError):
        return 0.0


def analyze_balance_sheet(text):
    """Анализ бухгалтерского баланса (российский формат)"""
    ratios = []

    # Коды строк баланса по российским стандартам
    balance_patterns = [
        (r'Внеоборотные активы.*?1100.*?([\d\s\(\)]+)', 'Внеоборотные активы'),
        (r'Оборотные активы.*?1200.*?([\d\s\(\)]+)', 'Оборотные активы'),
        (r'БАЛАНС.*?1600.*?([\d\s\(\)]+)', 'Активы всего'),
        (r'Капитал и резервы.*?1300.*?([\d\s\(\)]+)', 'Капитал'),
        (r'Долгосрочные обязательства.*?1400.*?([\d\s\(\)]+)', 'Долгосрочные обязательства'),
        (r'Краткосрочные обязательства.*?1500.*?([\d\s\(\)]+)', 'Краткосрочные обязательства'),
        (r'БАЛАНС.*?1700.*?([\d\s\(\)]+)', 'Пассивы всего'),
        (r'Денежные средства.*?1250.*?([\d\s\(\)]+)', 'Денежные средства'),
        (r'Запасы.*?1210.*?([\d\s\(\)]+)', 'Запасы'),
    ]

    values = {}
    for pattern, name in balance_patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            value_str = match.group(1).strip()
            values[name] = parse_financial_value(value_str)
            ratios.append((name, values[name]))

    # Расчет коэффициентов
    assets = values.get('Активы всего', 0)
    equity = values.get('Капитал', 0)
    current_assets = values.get('Оборотные активы', 0)
    current_liabilities = values.get('Краткосрочные обязательства', 0)
    cash = values.get('Денежные средства', 0)
    inventory = values.get('Запасы', 0)

    if current_liabilities and current_liabilities != 0:
        current_ratio = current_assets / current_liabilities
        ratios.append(('Коэффициент текущей ликвидности', current_ratio))

    if assets and assets != 0:
        autonomy_ratio = equity / assets
        ratios.append(('Коэффициент автономии', autonomy_ratio))

    if current_liabilities and current_liabilities != 0 and cash:
        cash_ratio = cash / current_liabilities
        ratios.append(('Коэффициент абсолютной ликвидности', cash_ratio))

    return ratios


def analyze_profit_loss_statement(text: str) -> List[Tuple[str, float]]:
    """Анализ отчета о финансовых результатах (российский формат)"""
    ratios = []

    # Коды строк отчета о финансовых результатах
    profit_patterns = [
        (r'Выручка.*?2110.*?([\d\s\(\)]+)', 'Выручка'),
        (r'Себестоимость продаж.*?2120.*?([\d\s\(\)]+)', 'Себестоимость'),
        (r'Валовая прибыль.*?2100.*?([\d\s\(\)]+)', 'Валовая прибыль'),
        (r'Коммерческие расходы.*?2210.*?([\d\s\(\)]+)', 'Коммерческие расходы'),
        (r'Управленческие расходы.*?2220.*?([\d\s\(\)]+)', 'Управленческие расходы'),
        (r'Прибыль от продаж.*?2200.*?([\d\s\(\)]+)', 'Прибыль от продаж'),
        (r'Налог на прибыль.*?2410.*?([\d\s\(\)]+)', 'Налог на прибыль'),
        (r'Чистая прибыль.*?2400.*?([\d\s\(\)]+)', 'Чистая прибыль'),
    ]

    values = {}
    for pattern, name in profit_patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            value_str = match.group(1).strip()
            values[name] = parse_financial_value(value_str)
            ratios.append((name, values[name]))

    # Расчет коэффициентов рентабельности
    revenue = values.get('Выручка', 0)
    cogs = values.get('Себестоимость', 0)
    operating_profit = values.get('Прибыль от продаж', 0)
    net_profit = values.get('Чистая прибыль', 0)

    if revenue and revenue != 0:
        if cogs:
            gross_margin = ((revenue + cogs) / revenue) * 100
            ratios.append(('Валовая рентабельность, %', gross_margin))

        if operating_profit:
            operating_margin = (operating_profit / revenue) * 100
            ratios.append(('Операционная рентабельность, %', operating_margin))

        if net_profit:
            net_margin = (net_profit / revenue) * 100
            ratios.append(('Чистая рентабельность, %', net_margin))

    return ratios


def analyze_cash_flow_statement(text):
    """Анализ отчета о движении денежных средств (российский формат)"""
    ratios = []

    # Коды строк отчета о движении денежных средств
    cash_flow_patterns = [
        (r'Денежные потоки от операционной деятельности.*?4100.*?([\d\s\(\)]+)', 'Операционная деятельность'),
        (r'Денежные потоки от инвестиционной деятельности.*?4200.*?([\d\s\(\)]+)', 'Инвестиционная деятельность'),
        (r'Денежные потоки от финансовой деятельности.*?4300.*?([\d\s\(\)]+)', 'Финансовая деятельность'),
        (r'Чистое увеличение.*?4400.*?([\d\s\(\)]+)', 'Чистый денежный поток'),
    ]

    values = {}
    for pattern, name in cash_flow_patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            value_str = match.group(1).strip()
            values[name] = parse_financial_value(value_str)
            ratios.append((name, values[name]))

    # Расчет дополнительных коэффициентов
    operating_cash = values.get('Операционная деятельность', 0)
    investing_cash = values.get('Инвестиционная деятельность', 0)
    net_cash = values.get('Чистый денежный поток', 0)

    if operating_cash and investing_cash:
        free_cash_flow = operating_cash + investing_cash
        ratios.append(('Свободный денежный поток', free_cash_flow))

    if net_cash and net_cash != 0 and operating_cash:
        cash_quality = operating_cash / net_cash
        ratios.append(('Качество денежных потоков', cash_quality))

    return ratios


def auto_detect_financial_data(text):
    """Автоматическое определение финансовных данных"""
    ratios = []

    # Поиск крупных денежных сумм (6+ цифр)
    numbers = re.findall(r'\b[\d\s]{6,}\b', text)
    for num_str in numbers[:5]:
        try:
            clean_num = num_str.replace(' ', '').replace(',', '.')
            value = float(clean_num)
            if abs(value) > 1000:
                ratios.append((f'Финансовый показатель {len(ratios) + 1}', value))
        except ValueError:
            continue

    return ratios


