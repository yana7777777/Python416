import re
import pdfplumber
from .models import BalanceSheetData, ProfitLossData, CashFlowData


def parse_financial_value(value_str):
    """Парсит финансовое значение из строки"""
    if not value_str or value_str in ['-', '—', ' ', '']:
        return None

    # Очищаем строку
    cleaned = value_str.replace(' ', '').replace('(', '-').replace(')', '')

    try:
        return float(cleaned)
    except ValueError:
        return None


def parse_table_structure(text, document_type):
    """Парсит табличную структуру: находит заголовки колонок и строки с данными"""
    lines = [line.strip() for line in text.split('\n') if line.strip()]

    # Определяем шаблоны для каждого типа документа
    configs = {
        'balance': {
            'year_headers': ['2024', '2023', '2022'],
            'column_pattern': r'На 31 декабря (\d{4}) г\.',
            'codes': ['1110', '1120', '1130', '1140', '1150', '1160', '1170', '1180', '1190',
                      '1100', '1210', '1220', '1230', '1240', '1250', '1260', '1200', '1600',
                      '1310', '1320', '1340', '1350', '1360', '1370', '1300',
                      '1410', '1420', '1430', '1450', '1400',
                      '1510', '1520', '1530', '1540', '1550', '1500', '1700']
        },
        'profit_loss': {
            'year_headers': ['2024', '2023'],
            'column_pattern': r'За январь-декабрь (\d{4}) г\.',
            'codes': ['2110', '2120', '2100', '2210', '2220', '2200', '2310', '2320', '2330',
                      '2340', '2350', '2300', '2410', '2421', '2430', '2450', '2460', '2400']
        },
        'cash_flow': {
            'year_headers': ['2024', '2023'],
            'column_pattern': r'За январь-декабрь (\d{4}) г\.',
            'codes': ['4110', '4120', '4100', '4210', '4220', '4200', '4310', '4320', '4300', '4400']
        }
    }

    config = configs.get(document_type)
    if not config:
        return []

    # Ищем строку с заголовками колонок (годами)
    header_line_index = -1
    column_positions = {}

    for i, line in enumerate(lines):
        if any(year in line for year in config['year_headers']):
            header_line_index = i
            # Разбиваем строку на колонки по разделителям
            columns = re.split(r'\s*\|\s*', line)
            for idx, col in enumerate(columns):
                for year in config['year_headers']:
                    if year in col:
                        column_positions[year] = idx
            break

    if header_line_index == -1:
        return []

    # Теперь ищем строки с кодами и данными
    data = []

    for i in range(header_line_index + 1, len(lines)):
        line = lines[i]

        # Проверяем, есть ли в строке код
        for code in config['codes']:
            if code in line:
                # Разбиваем строку на ячейки
                cells = re.split(r'\s*\|\s*', line)

                # Ищем название показателя (обычно в предыдущей строке)
                name = "Неизвестно"
                if i > 0:
                    prev_line = lines[i - 1]
                    # Извлекаем текст названия (между | и |)
                    name_match = re.search(r'\|\s*([^|]+?)\s*\|\s*' + code, line)
                    if not name_match and i > 1:
                        # Пробуем взять всю предыдущую строку как название
                        name = lines[i - 1].strip('| ').split('|')[0].strip()

                # Ищем значения в ячейках согласно позициям колонок
                row_data = {'code': code, 'name': name}

                for year, col_idx in column_positions.items():
                    if col_idx < len(cells):
                        value_str = cells[col_idx].strip()
                        value = parse_financial_value(value_str)
                        if value is not None:
                            row_data[year] = value

                data.append(row_data)
                break

    return data


def parse_balance_sheet(text, document):
    """Парсинг бухгалтерского баланса - ПРАВИЛЬНЫЙ ПАРСИНГ ПО КОЛОНКАМ"""
    BalanceSheetData.objects.filter(document=document).delete()

    print("=== ПАРСИНГ БАЛАНСА ===")
    print(f"Размер текста: {len(text)} символов")

    data = parse_table_structure(text, 'balance')

    print(f"Найдено строк: {len(data)}")

    for row in data:
        print(f"Строка: {row['code']} - {row.get('2022')} | {row.get('2023')} | {row.get('2024')}")

        BalanceSheetData.objects.create(
            document=document,
            code=row['code'],
            name=row['name'],
            value_2022=row.get('2022'),
            value_2023=row.get('2023'),
            value_2024=row.get('2024')
        )

    return len(data) > 0


def parse_profit_loss(text, document):
    """Парсинг отчета о финансовых результатах - ПРАВИЛЬНЫЙ ПАРСИНГ ПО КОЛОНКАМ"""
    ProfitLossData.objects.filter(document=document).delete()

    print("=== ПАРСИНГ ОТЧЕТА О ПРИБЫЛЯХ ===")

    data = parse_table_structure(text, 'profit_loss')

    print(f"Найдено строк: {len(data)}")

    for row in data:
        print(f"Строка: {row['code']} - {row.get('2023')} | {row.get('2024')}")

        ProfitLossData.objects.create(
            document=document,
            code=row['code'],
            name=row['name'],
            value_2023=row.get('2023'),
            value_2024=row.get('2024')
        )

    return len(data) > 0


def parse_cash_flow(text, document):
    """Парсинг отчета о движении денежных средств - ПРАВИЛЬНЫЙ ПАРСИНГ ПО КОЛОНКАМ"""
    CashFlowData.objects.filter(document=document).delete()

    print("=== ПАРСИНГ ОТЧЕТА О ДЕНЕЖНЫХ СРЕДСТВАХ ===")

    data = parse_table_structure(text, 'cash_flow')

    print(f"Найдено строк: {len(data)}")

    for row in data:
        print(f"Строка: {row['code']} - {row.get('2023')} | {row.get('2024')}")

        CashFlowData.objects.create(
            document=document,
            code=row['code'],
            name=row['name'],
            value_2023=row.get('2023'),
            value_2024=row.get('2024')
        )

    return len(data) > 0


def extract_text_with_table_detection(pdf_path):
    """Извлечение текста с учетом табличной структуры"""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                # Пробуем разные стратегии извлечения
                strategies = [
                    lambda p: p.extract_text(layout=False),  # Без layout
                    lambda p: p.extract_text(layout=True),  # С layout
                    lambda p: p.extract_text(x_tolerance=2, y_tolerance=2),  # С допусками
                ]

                for strategy in strategies:
                    try:
                        page_text = strategy(page)
                        if page_text and len(page_text.strip()) > 100:  # Достаточно текста
                            text += f"=== СТРАНИЦА {page_num + 1} ===\n"
                            text += page_text + "\n\n"
                            break
                    except:
                        continue

    except Exception as e:
        print(f"Ошибка чтения PDF: {e}")

    return text