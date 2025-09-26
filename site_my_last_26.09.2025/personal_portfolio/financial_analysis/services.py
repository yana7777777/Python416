from .models import BalanceSheetData, ProfitLossData, CashFlowData, FinancialRatio


class BalanceSheetAnalyzer:
    def __init__(self, document):
        self.document = document
        self.data = self._load_data()

    def _load_data(self):
        """Загружает все данные баланса и выводит для отладки"""
        data = {}
        items = BalanceSheetData.objects.filter(document=self.document)

        print("=== ДАННЫЕ БАЛАНСА ИЗ БАЗЫ ===")
        for item in items:
            print(f"{item.code} - {item.name}: 2022={item.value_2022}, 2023={item.value_2023}, 2024={item.value_2024}")
            data[item.code] = {
                'name': item.name,
                '2022': item.value_2022 or 0,
                '2023': item.value_2023 or 0,
                '2024': item.value_2024 or 0
            }

        return data

    def calculate_basic_ratios(self):
        """Рассчитывает базовые коэффициенты для всех годов"""
        ratios = []

        for year in [2022, 2023, 2024]:
            # Получаем ключевые показатели
            assets = self.data.get('1600', {}).get(str(year), 0)
            equity = self.data.get('1300', {}).get(str(year), 0)
            current_assets = self.data.get('1200', {}).get(str(year), 0)
            current_liabilities = self.data.get('1500', {}).get(str(year), 0)

            year_ratios = {}

            # Коэффициент текущей ликвидности
            if current_liabilities and current_liabilities != 0:
                current_ratio = current_assets / current_liabilities
                year_ratios['Коэффициент текущей ликвидности'] = current_ratio
            else:
                year_ratios['Коэффициент текущей ликвидности'] = 0

            # Коэффициент автономии
            if assets and assets != 0:
                autonomy_ratio = equity / assets
                year_ratios['Коэффициент автономии'] = autonomy_ratio
            else:
                year_ratios['Коэффициент автономии'] = 0

            # Абсолютные показатели
            year_ratios['Активы всего'] = assets
            year_ratios['Собственный капитал'] = equity
            year_ratios['Оборотные активы'] = current_assets
            year_ratios['Краткосрочные обязательства'] = current_liabilities

            ratios.append({'year': year, 'ratios': year_ratios})

        return ratios

    def save_ratios(self):
        FinancialRatio.objects.filter(document=self.document).delete()

        ratios_data = self.calculate_basic_ratios()

        print("=== РАССЧИТАННЫЕ КОЭФФИЦИЕНТЫ ===")
        for year_data in ratios_data:
            year = year_data['year']
            ratios = year_data['ratios']

            for name, value in ratios.items():
                print(f"{name} ({year}): {value}")

                FinancialRatio.objects.create(
                    document=self.document,
                    ratio_name=f"{name} ({year} г.)",
                    ratio_value=float(value),
                    year=year
                )


# Аналогичные упрощенные классы для других отчетов
class ProfitLossAnalyzer:
    def __init__(self, document):
        self.document = document
        self.data = self._load_data()

    def _load_data(self):
        data = {}
        items = ProfitLossData.objects.filter(document=self.document)

        print("=== ДАННЫЕ ОТЧЕТА О ПРИБЫЛЯХ ИЗ БАЗЫ ===")
        for item in items:
            print(f"{item.code} - {item.name}: 2023={item.value_2023}, 2024={item.value_2024}")
            data[item.code] = {
                'name': item.name,
                '2023': item.value_2023 or 0,
                '2024': item.value_2024 or 0
            }

        return data

    def save_ratios(self):
        FinancialRatio.objects.filter(document=self.document).delete()

        revenue_2023 = self.data.get('2110', {}).get('2023', 0)
        revenue_2024 = self.data.get('2110', {}).get('2024', 0)
        net_profit_2023 = self.data.get('2400', {}).get('2023', 0)
        net_profit_2024 = self.data.get('2400', {}).get('2024', 0)

        ratios = [
            ('Выручка 2023', revenue_2023),
            ('Выручка 2024', revenue_2024),
            ('Чистая прибыль 2023', net_profit_2023),
            ('Чистая прибыль 2024', net_profit_2024),
        ]

        if revenue_2023 != 0:
            profitability_2023 = (net_profit_2023 / revenue_2023) * 100
            ratios.append(('Рентабельность 2023, %', profitability_2023))

        if revenue_2024 != 0:
            profitability_2024 = (net_profit_2024 / revenue_2024) * 100
            ratios.append(('Рентабельность 2024, %', profitability_2024))

        for name, value in ratios:
            FinancialRatio.objects.create(
                document=self.document,
                ratio_name=name,
                ratio_value=float(value),
                year=2024
            )


class CashFlowAnalyzer:
    def __init__(self, document):
        self.document = document
        self.data = self._load_data()

    def _load_data(self):
        data = {}
        items = CashFlowData.objects.filter(document=self.document)

        print("=== ДАННЫЕ ОТЧЕТА О ДЕНЕЖНЫХ СРЕДСТВАХ ИЗ БАЗЫ ===")
        for item in items:
            print(f"{item.code} - {item.name}: 2023={item.value_2023}, 2024={item.value_2024}")
            data[item.code] = {
                'name': item.name,
                '2023': item.value_2023 or 0,
                '2024': item.value_2024 or 0
            }

        return data

    def save_ratios(self):
        FinancialRatio.objects.filter(document=self.document).delete()

        operating_2023 = self.data.get('4100', {}).get('2023', 0)
        operating_2024 = self.data.get('4100', {}).get('2024', 0)

        ratios = [
            ('Операционный поток 2023', operating_2023),
            ('Операционный поток 2024', operating_2024),
        ]

        for name, value in ratios:
            FinancialRatio.objects.create(
                document=self.document,
                ratio_name=name,
                ratio_value=float(value),
                year=2024
            )