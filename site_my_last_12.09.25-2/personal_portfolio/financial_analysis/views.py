from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FinancialDocumentForm
from .models import FinancialDocument, FinancialRatio
import pdfplumber
import re


@login_required
def upload_document(request):
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


def analyze_document(document):
    ratios = []

    try:
        with pdfplumber.open(document.pdf_file.path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"

            # Парсим финансовые данные (пример для баланса)
            assets = extract_value(text, "Актив", "Итого по разделу")
            liabilities = extract_value(text, "Пассив", "Итого по разделу")
            revenue = extract_value(text, "Выручка", "руб")
            profit = extract_value(text, "Прибыль", "руб")

            # Рассчитываем коэффициенты
            if assets and liabilities:
                current_ratio = float(assets) / float(liabilities)
                ratios.append(('Коэффициент текущей ликвидности', current_ratio))

            if revenue and profit:
                profitability = (float(profit) / float(revenue)) * 100
                ratios.append(('Рентабельность продаж (%)', profitability))

    except Exception as e:
        print(f"Ошибка анализа документа: {e}")

        # Сохраняем коэффициенты в базу
    for ratio_name, ratio_value in ratios:
        FinancialRatio.objects.create(
            document=document,
            ratio_name=ratio_name,
            ratio_value=ratio_value
        )


def extract_value(text, start_pattern, end_pattern):
    """Извлекает числовое значение из текста между паттернами"""
    pattern = f"{start_pattern}.*?([\\d\\s,]+)\\s*{end_pattern}"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    if match:
        value = match.group(1).replace(' ', '').replace(',', '.')
        try:
            return float(value)
        except ValueError:
            return None
    return None


@login_required
def financial_results(request, document_id):
    document = FinancialDocument.objects.get(id=document_id, user=request.user)
    ratios = FinancialRatio.objects.filter(document=document)

    return render(request, 'financial_analysis/results.html', {
        'document': document,
        'ratios': ratios
    })


@login_required
def document_list(request):
    documents = FinancialDocument.objects.filter(user=request.user)
    return render(request, 'financial_analysis/list.html', {'documents': documents})