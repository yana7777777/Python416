from django import forms
from .models import FinancialDocument


class FinancialDocumentForm(forms.ModelForm):
    class Meta:
        model = FinancialDocument
        fields = ['title', 'document_type', 'pdf_file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'document_type': forms.Select(attrs={'class': 'form-control'}),
            'pdf_file': forms.FileInput(attrs={'class': 'form-control'}),
        }