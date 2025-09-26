from django.contrib import admin
from .models import FinancialDocument, FinancialRatio, BalanceSheetData, ProfitLossData, CashFlowData


@admin.register(FinancialDocument)
class FinancialDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'document_type', 'upload_date']


@admin.register(FinancialRatio)
class FinancialRatioAdmin(admin.ModelAdmin):
    list_display = ['ratio_name', 'ratio_value', 'document', 'year']


@admin.register(BalanceSheetData)
class BalanceSheetDataAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'value_2022', 'value_2023', 'value_2024', 'document']


@admin.register(ProfitLossData)
class ProfitLossDataAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'value_2023', 'value_2024', 'document']


@admin.register(CashFlowData)
class CashFlowDataAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'value_2023', 'value_2024', 'document']
