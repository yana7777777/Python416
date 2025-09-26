from django.db import models
from django.contrib.auth.models import User


class FinancialDocument(models.Model):
    DOCUMENT_TYPES = [
        ('balance', 'Бухгалтерский баланс'),
        ('profit_loss', 'Отчет о финансовых результатах'),
        ('cash_flow', 'Отчет о движении денежных средств'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    pdf_file = models.FileField(upload_to='financial_docs/')
    upload_date = models.DateTimeField(auto_now_add=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


# Модель для хранения распарсенных строк баланса
class BalanceSheetData(models.Model):
    document = models.ForeignKey(FinancialDocument, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, verbose_name="Код строки")
    name = models.TextField(verbose_name="Наименование показателя")
    value_2022 = models.FloatField(null=True, blank=True)
    value_2023 = models.FloatField(null=True, blank=True)
    value_2024 = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ['document', 'code']

    def __str__(self):
        return f"{self.code} - {self.name}"


# Модель для отчета о финансовых результатах
class ProfitLossData(models.Model):
    document = models.ForeignKey(FinancialDocument, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, verbose_name="Код строки")
    name = models.TextField(verbose_name="Наименование показателя")
    value_2023 = models.FloatField(null=True, blank=True)
    value_2024 = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ['document', 'code']

    def __str__(self):
        return f"{self.code} - {self.name}"


# Модель для отчета о движении денежных средств
class CashFlowData(models.Model):
    document = models.ForeignKey(FinancialDocument, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, verbose_name="Код строки")
    name = models.TextField(verbose_name="Наименование показателя")
    value_2023 = models.FloatField(null=True, blank=True)
    value_2024 = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ['document', 'code']

    def __str__(self):
        return f"{self.code} - {self.name}"


class FinancialRatio(models.Model):
    document = models.ForeignKey(FinancialDocument, on_delete=models.CASCADE)
    ratio_name = models.CharField(max_length=100)
    ratio_value = models.FloatField()
    calculation_date = models.DateTimeField(auto_now_add=True)
    year = models.IntegerField(verbose_name="Год расчета")

    def save(self, *args, **kwargs):
        if hasattr(self.ratio_value, 'as_integer_ratio'):
            self.ratio_value = float(self.ratio_value)
        elif isinstance(self.ratio_value, str):
            try:
                self.ratio_value = float(self.ratio_value)
            except (ValueError, TypeError):
                self.ratio_value = 0.0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ratio_name}: {self.ratio_value}"