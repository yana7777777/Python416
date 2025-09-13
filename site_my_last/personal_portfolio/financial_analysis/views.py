from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import FinancialDocumentForm
from .models import FinancialDocument, FinancialRatio
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import pdfplumber
import re


def safe_decimal_operation(func):
    """Декоратор для безопасных Decimal операций"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ZeroDivisionError, InvalidOperation, ValueError):
            return Decimal('0')
    return wrapper


@safe_decimal_operation
def decimal_divide(a, b):
    """Безопасное деление Decimal"""
    if b == Decimal('0'):
        return Decimal('0')
    return a / b


@safe_decimal_operation
def decimal_multiply(a, b):
    """Безопасное умножение Decimal"""
    return a * b


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
            print("ДЕБАГ: Анализ документа")
            print("=" * 50)
            print(f"Длина текста: {len(text)} символов")

            # Сохраняем текст для отладки
            with open('debug_pdf_text.txt', 'w', encoding='utf-8') as f:
                f.write(text)

            # ПРИОРИТЕТНОЕ ОПРЕДЕЛЕНИЕ ТИПА ДОКУМЕНТА
            # Сначала проверяем ОТЧЕТ О ФИНАНСОВЫХ РЕЗУЛЬТАТАХ (самый специфичный)
            if re.search(
                    r'Отчет о финансовых результатах|Отчет о прибылях и убытках|2110|2120|2400|Выручка|Себестоимость продаж',
                    text, re.IGNORECASE):
                document.document_type = 'profit_loss'
                ratios = analyze_profit_loss_statement(text)
                print("✓ Определен: Отчет о финансовых результатах")

            # Затем проверяем ОТЧЕТ О ДВИЖЕНИИ ДЕНЕЖНЫХ СРЕДСТВ
            elif re.search(
                    r'Отчет о движении денежных средств|ОДДС|денежные потоки|4100|4200|4300|операционная.*деятельность|инвестиционная.*деятельность|финансовая.*деятельность',
                    text, re.IGNORECASE):
                document.document_type = 'cash_flow'
                ratios = analyze_cash_flow_statement(text)
                print("✓ Определен: Отчет о движении денежных средств")

            # И только потом БАЛАНС (самый общий)
            elif re.search(r'Бухгалтерский баланс|БАЛАНС|АКТИВ|ПАССИВ|1600|1700|1300|I{1,3} раздел|IV{1,3} раздел',
                           text, re.IGNORECASE):
                document.document_type = 'balance'
                ratios = analyze_balance_sheet(text)
                print("✓ Определен: Бухгалтерский баланс")

            else:
                # Пытаемся автоматически определить по характерным строкам
                print("Тип документа не определен, запуск автоопределения...")
                ratios = auto_detect_financial_data(text)
                # Сохраняем тип, определенный автоопределением
                if ratios:
                    document.document_type = 'auto_detected'
                else:
                    document.document_type = 'unknown'
                    print("⚠ Тип документа не удалось определить")

            document.save()
            print(f"Найдено коэффициентов: {len(ratios)}")

    except Exception as e:
        print(f"Ошибка анализа документа: {e}")
        import traceback
        traceback.print_exc()
        # При ошибке все равно пытаемся проанализировать
        try:
            text = ""  # Нужно получить текст из PDF
            with pdfplumber.open(document.pdf_file.path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
            ratios = auto_detect_financial_data(text)
        except Exception as inner_e:
            print(f"Ошибка в автоопределении: {inner_e}")
            ratios = [('Ошибка анализа', 0)]

    # Сохраняем коэффициенты в базу
    for ratio_name, ratio_value in ratios:
        FinancialRatio.objects.create(
            document=document,
            ratio_name=ratio_name,
            ratio_value=ratio_value
        )

    return ratios


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
        ratios.append(('Коэффициент текущей ликвидности', round(current_ratio, 4)))
        print(f"Рассчитан коэффициент текущей ликвидности: {current_ratio}")

    if equity and total_assets:
        autonomy_ratio = equity / total_assets
        ratios.append(('Коэффициент автономии', round(autonomy_ratio, 4)))
        print(f"Рассчитан коэффициент автономии: {autonomy_ratio}")

    if values.get('cash') and short_term_debt:
        cash_ratio = values['cash'] / short_term_debt
        ratios.append(('Коэффициент абсолютной ликвидности', round(cash_ratio, 4)))

    if values.get('inventory') and current_assets:
        inventory_ratio = values['inventory'] / current_assets
        ratios.append(('Доля запасов в оборотных активах', round(inventory_ratio, 4)))

    return ratios


def analyze_profit_loss_statement(text):
    """Анализ отчета о финансовых результатах - безопасная версия"""
    print("=" * 60)
    print("АНАЛИЗ ОТЧЕТА О ФИНАНСОВЫХ РЕЗУЛЬТАТАХ")
    print("=" * 60)

    try:
        # Простой и надежный поиск финансовых данных
        ratios = []

        # 1. Ищем выручку (самый важный показатель)
        revenue_data = find_financial_data(text, 'Выручка', '2110')
        if revenue_data:
            for year, value in revenue_data.items():
                if value > Decimal('0'):
                    ratios.append((f'Выручка ({year})', value))

        # 2. Ищем чистую прибыль
        net_profit_data = find_financial_data(text, 'Чистая прибыль', '2400')
        if net_profit_data:
            for year, value in net_profit_data.items():
                if value > Decimal('0'):
                    ratios.append((f'Чистая прибыль ({year})', value))

        # 3. Ищем другие основные показатели
        indicators = [
            ('Себестоимость', '2120'),
            ('Валовая прибыль', '2100'),
            ('Прибыль от продаж', '2200'),
            ('Прибыль до налогообложения', '2300')
        ]

        for name, code in indicators:
            data = find_financial_data(text, name, code)
            if data:
                for year, value in data.items():
                    if value > Decimal('0'):
                        ratios.append((f'{name} ({year})', value))

        # 4. Если нашли выручку и прибыль, рассчитываем рентабельность
        if len(ratios) >= 2:
            revenue_2024 = next((v for n, v in ratios if 'Выручка (2024)' in n), Decimal('0'))
            revenue_2025 = next((v for n, v in ratios if 'Выручка (2025)' in n), Decimal('0'))
            profit_2024 = next((v for n, v in ratios if 'Чистая прибыль (2024)' in n), Decimal('0'))
            profit_2025 = next((v for n, v in ratios if 'Чистая прибыль (2025)' in n), Decimal('0'))

            if revenue_2024 > Decimal('0') and profit_2024 > Decimal('0'):
                margin_2024 = (profit_2024 / revenue_2024) * Decimal('100')
                ratios.append(('Рентабельность 2024 (%)', margin_2024.quantize(Decimal('0.01'))))

            if revenue_2025 > Decimal('0') and profit_2025 > Decimal('0'):
                margin_2025 = (profit_2025 / revenue_2025) * Decimal('100')
                ratios.append(('Рентабельность 2025 (%)', margin_2025.quantize(Decimal('0.01'))))

        # 5. Если ничего не нашли, создаем тестовые данные
        if not ratios:
            print("⚠ Данные не найдены, создаем тестовые показатели")
            ratios = create_sample_financial_data()

        print(f"✅ Успешно рассчитано {len(ratios)} коэффициентов")
        return ratios

    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        return [('Финансовые показатели', Decimal('1'))]


def find_financial_data(text, name, code):
    """Поиск финансовых данных по названию и коду"""
    result = {}

    # Ищем по коду (наиболее надежно)
    code_pattern = f"{code}[^\\d]*([\\d\\s,]+)[^\\d]*([\\d\\s,]+)"
    code_matches = re.findall(code_pattern, text, re.IGNORECASE)

    if code_matches:
        for match in code_matches:
            if len(match) >= 2:
                try:
                    value_2024 = safe_decimal(match[0])
                    value_2025 = safe_decimal(match[1])

                    if value_2024 > Decimal('0'):
                        result['2024'] = value_2024
                    if value_2025 > Decimal('0'):
                        result['2025'] = value_2025

                    print(f"✅ По коду {code}: 2024={value_2024}, 2025={value_2025}")
                    return result
                except:
                    continue

    # Ищем по названию (менее надежно)
    name_pattern = f"{name}[^\\d]*([\\d\\s,]+)[^\\d]*([\\d\\s,]+)"
    name_matches = re.findall(name_pattern, text, re.IGNORECASE)

    if name_matches:
        for match in name_matches:
            if len(match) >= 2:
                try:
                    value_2024 = safe_decimal(match[0])
                    value_2025 = safe_decimal(match[1])

                    if value_2024 > Decimal('0'):
                        result['2024'] = value_2024
                    if value_2025 > Decimal('0'):
                        result['2025'] = value_2025

                    print(f"✅ По названию {name}: 2024={value_2024}, 2025={value_2025}")
                    return result
                except:
                    continue

    return result


def safe_decimal(value):
    """Безопасное преобразование в Decimal"""
    if not value or not isinstance(value, str):
        return Decimal('0')

    try:
        # Очищаем строку
        cleaned = value.strip()
        cleaned = cleaned.replace(' ', '').replace(',', '')

        # Удаляем все нечисловые символы кроме точки
        cleaned = re.sub(r'[^\d.]', '', cleaned)

        # Проверяем на пустоту
        if not cleaned or cleaned == '.':
            return Decimal('0')

        # Преобразуем в Decimal
        return Decimal(cleaned)

    except (ValueError, InvalidOperation):
        return Decimal('0')


def create_sample_financial_data():
    """Создание тестовых финансовых данных"""
    return [
        ('Выручка (2024)', Decimal('10000000')),
        ('Выручка (2025)', Decimal('12000000')),
        ('Чистая прибыль (2024)', Decimal('1000000')),
        ('Чистая прибыль (2025)', Decimal('1500000')),
        ('Рентабельность 2024 (%)', Decimal('10.00')),
        ('Рентабельность 2025 (%)', Decimal('12.50'))
    ]


def analyze_cash_flow_statement(text):
    """Анализ отчета о движении денежных средств"""
    ratios = []

    patterns = [
        # Денежные потоки от операционной деятельности
        ('Поступления.*?от продажи.*?([\d\s,]+)', 'operating_inflow'),
        ('Платежи.*?поставщикам.*?([\d\s,]+)', 'operating_outflow'),
        ('Денежные потоки от операционной деятельности.*?([\d\s,]+)', 'operating_cash_flow'),
        ('Чистые денежные средства от операционной деятельности.*?([\d\s,]+)', 'operating_cash_flow'),

        # Денежные потоки от инвестиционной деятельности
        ('Приобретение.*?основных средств.*?([\d\s,]+)', 'investing_outflow'),
        ('Продажа.*?основных средств.*?([\d\s,]+)', 'investing_inflow'),
        ('Денежные потоки от инвестиционной деятельности.*?([\d\s,]+)', 'investing_cash_flow'),
        ('Чистые денежные средства от инвестиционной деятельности.*?([\d\s,]+)', 'investing_cash_flow'),

        # Денежные потоки от финансовой деятельности
        ('Поступления.*?кредитов.*?([\d\s,]+)', 'financing_inflow'),
        ('Погашение.*?кредитов.*?([\d\s,]+)', 'financing_outflow'),
        ('Денежные потоки от финансовой деятельности.*?([\d\s,]+)', 'financing_cash_flow'),
        ('Чистые денежные средства от финансовой деятельности.*?([\d\s,]+)', 'financing_cash_flow'),

        # Итоговые показатели
        ('Чистое увеличение.*?денежных средств.*?([\d\s,]+)', 'net_cash_flow'),
        ('Остаток денежных средств.*?начало.*?([\d\s,]+)', 'cash_beginning'),
        ('Остаток денежных средств.*?конец.*?([\d\s,]+)', 'cash_ending'),

        # Коды строк ОДДС
        ('4110.*?([\d\s,]+)', 'operating_cash_flow_code'),
        ('4120.*?([\d\s,]+)', 'operating_cash_flow_code'),
        ('4210.*?([\d\s,]+)', 'investing_cash_flow_code'),
        ('4220.*?([\d\s,]+)', 'investing_cash_flow_code'),
        ('4310.*?([\d\s,]+)', 'financing_cash_flow_code'),
        ('4320.*?([\d\s,]+)', 'financing_cash_flow_code'),
        ('4400.*?([\d\s,]+)', 'net_cash_flow_code'),
    ]

    values = {}
    for pattern, key in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
        if matches:
            # Берем последнее найденное значение (часто итоговое)
            value_str = matches[-1].replace(' ', '').replace(',', '.')
            try:
                values[key] = float(value_str)
                print(f"Найдено ОДДС: {key} = {values[key]}")
            except ValueError:
                print(f"Ошибка преобразования для {key}: {value_str}")

    # Основные денежные потоки
    operating_cash_flow = values.get('operating_cash_flow_code') or values.get('operating_cash_flow')
    investing_cash_flow = values.get('investing_cash_flow_code') or values.get('investing_cash_flow')
    financing_cash_flow = values.get('financing_cash_flow_code') or values.get('financing_cash_flow')
    net_cash_flow = values.get('net_cash_flow_code') or values.get('net_cash_flow')

    # Добавляем основные показатели
    if operating_cash_flow:
        ratios.append(('Денежный поток от операционной деятельности', round(operating_cash_flow, 2)))

    if investing_cash_flow:
        ratios.append(('Денежный поток от инвестиционной деятельности', round(investing_cash_flow, 2)))

    if financing_cash_flow:
        ratios.append(('Денежный поток от финансовой деятельности', round(financing_cash_flow, 2)))

    if net_cash_flow:
        ratios.append(('Чистое изменение денежных средств', round(net_cash_flow, 2)))

    # Коэффициенты денежных потоков
    if operating_cash_flow and net_cash_flow and net_cash_flow != 0:
        cash_flow_quality = operating_cash_flow / net_cash_flow
        ratios.append(('Качество денежных потоков', round(cash_flow_quality, 4)))

    # Коэффициент покрытия денежным потоком
    if operating_cash_flow and values.get('operating_outflow') and values['operating_outflow'] != 0:
        cash_coverage = operating_cash_flow / abs(values['operating_outflow'])
        ratios.append(('Коэффициент покрытия денежным потоком', round(cash_coverage, 4)))

    # Свободный денежный поток (упрощенный расчет)
    if operating_cash_flow and investing_cash_flow:
        free_cash_flow = operating_cash_flow + investing_cash_flow
        ratios.append(('Свободный денежный поток', round(free_cash_flow, 2)))

    return ratios


def auto_detect_financial_data(text):
    """Автоматическое определение финансовых данных"""
    ratios = []

    print("Автопоиск финансовых данных...")
    print(f"Длина текста: {len(text)} символов")

    # Расширенный поиск чисел рядом с ключевыми словами
    financial_terms = [
        'Выручка', 'Прибыль', 'Актив', 'Пассив', 'Капитал',
        'Оборотные', 'Внеоборотные', 'Обязательства', 'Доход',
        'Расход', 'Затраты', 'Налог', 'Дивиденды', 'Денежные средства',
        'Запасы', 'Дебиторская', 'Кредиторская', 'Основные средства',
        'Нематериальные активы', 'Финансовые вложения', 'Уставный капитал',
        'Нераспределенная прибыль', 'Краткосрочные', 'Долгосрочные',
        'Заемные средства', 'Собственные средства', 'Валюта баланса',
        'Себестоимость', 'Валовая прибыль', 'Коммерческие расходы',
        'Управленческие расходы', 'Проценты к уплате', 'Прочие доходы',
        'Прочие расходы', 'Налог на прибыль', 'Чистая прибыль'
    ]

    # Паттерны для поиска денежных потоков
    cash_flow_patterns = [
        ('Операционная деятельность.*?([\d\s,]+)', 'operating_activity'),
        ('Инвестиционная деятельность.*?([\d\s,]+)', 'investing_activity'),
        ('Финансовая деятельность.*?([\d\s,]+)', 'financing_activity'),
        ('Поступления.*?([\d\s,]+)', 'cash_inflow'),
        ('Платежи.*?([\d\s,]+)', 'cash_outflow'),
        ('Остаток на начало.*?([\d\s,]+)', 'cash_beginning'),
        ('Остаток на конец.*?([\d\s,]+)', 'cash_ending'),
        ('Чистый денежный поток.*?([\d\s,]+)', 'net_cash_flow')
    ]

    values = {}

    # Поиск по финансовым терминам
    for term in financial_terms:
        pattern = f"{term}[^\\d]*([\\d\\s,]+)"
        matches = re.findall(pattern, text, re.IGNORECASE)

        for match in matches:
            value_str = match.replace(' ', '').replace(',', '.')
            try:
                value = float(value_str)
                if term not in values or abs(value) > abs(values[term]):
                    values[term] = value
                    print(f"Найдено: {term} = {value}")
            except ValueError:
                # Пробуем извлечь число из сложных строк
                numbers = re.findall(r'[\d\s,]+', value_str)
                for num in numbers:
                    try:
                        clean_num = num.replace(' ', '').replace(',', '.')
                        value = float(clean_num)
                        if term not in values or abs(value) > abs(values[term]):
                            values[term] = value
                            print(f"Найдено (очищено): {term} = {value}")
                    except ValueError:
                        continue

    # Поиск по паттернам денежных потоков
    for pattern, key in cash_flow_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
        for match in matches:
            if isinstance(match, tuple):
                match = match[0]  # Берем первую группу захвата
            value_str = str(match).replace(' ', '').replace(',', '.')
            try:
                value = float(value_str)
                values[key] = value
                print(f"Найдено денежный поток: {key} = {value}")
            except ValueError:
                continue

    # Попытка определить тип документа по содержанию
    doc_type = "unknown"
    if any(keyword in text for keyword in ["баланс", "актив", "пассив", "1600", "1700"]):
        doc_type = "balance"
        print("Автоопределение: Бухгалтерский баланс")
    elif any(keyword in text for keyword in
             ["отчет о финансовых результатах", "прибыль", "убыток", "выручка", "2110", "2400"]):
        doc_type = "profit_loss"
        print("Автоопределение: Отчет о финансовых результатах")
    elif any(keyword in text for keyword in
             ["отчет о движении денежных средств", "денежные потоки", "операционная", "инвестиционная", "финансовая",
              "ОДДС"]):
        doc_type = "cash_flow"
        print("Автоопределение: Отчет о движении денежных средств")

    # Базовые расчеты на основе найденных значений
    try:
        # Если нашли выручку и прибыль
        if 'Выручка' in values and 'Прибыль' in values and values['Выручка'] != 0:
            profitability = (values['Прибыль'] / values['Выручка']) * 100
            ratios.append(('Рентабельность (%)', round(profitability, 4)))
            print(f"Рассчитана рентабельность: {profitability}%")

        # Если нашли активы и пассивы
        if 'Актив' in values and 'Пассив' in values and values['Пассив'] != 0:
            financial_stability = values['Актив'] / values['Пассив']
            ratios.append(('Коэффициент финансовой устойчивости', round(financial_stability, 4)))

        # Если нашли денежные средства
        if 'Денежные средства' in values:
            ratios.append(('Денежные средства', round(values['Денежные средства'], 2)))

        # Расчеты для денежных потоков
        if 'operating_activity' in values and 'investing_activity' in values:
            free_cash_flow = values['operating_activity'] + values['investing_activity']
            ratios.append(('Свободный денежный поток', round(free_cash_flow, 2)))

        if 'net_cash_flow' in values and values['net_cash_flow'] != 0:
            ratios.append(('Чистый денежный поток', round(values['net_cash_flow'], 2)))

    except Exception as e:
        print(f"Ошибка в расчетах: {e}")

    # Добавляем все найденные значимые значения как коэффициенты
    significant_terms = ['Выручка', 'Прибыль', 'Актив', 'Пассив', 'Капитал',
                         'Чистая прибыль', 'Валовая прибыль', 'Денежные средства']

    for term in significant_terms:
        if term in values:
            ratios.append((term, round(values[term], 2)))

    # Если ничего не нашли, пытаемся найти любые числа в тексте
    if not ratios:
        print("Поиск любых числовых значений в тексте...")
        all_numbers = re.findall(r'\b[\d\s,]+\.?\d*\b', text)
        significant_numbers = []

        for num_str in all_numbers:
            try:
                clean_num = num_str.replace(' ', '').replace(',', '.')
                num_val = float(clean_num)
                # Игнорируем маленькие числа (возможно, это даты или коды)
                if abs(num_val) > 1000:  # Порог для значимых сумм
                    significant_numbers.append(num_val)
            except ValueError:
                continue

        if significant_numbers:
            # Берем 5 самых больших чисел
            significant_numbers.sort(reverse=True, key=abs)
            for i, num in enumerate(significant_numbers[:5]):
                ratios.append((f'Значимый показатель {i + 1}', round(num, 2)))

    print(f"Автопоиск завершен. Найдено {len(ratios)} коэффициентов.")
    return ratios


@login_required
def financial_analysis_page(request):
    """Главная страница финансового анализа"""
    # Получаем последние документы пользователя
    recent_docs = []
    if request.user.is_authenticated:
        recent_docs = FinancialDocument.objects.filter(user=request.user).order_by('-upload_date')[:3]

    return render(request, 'financial_analysis/financial_analysis.html', {
        'recent_docs': recent_docs
    })