from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_document, name='financial_upload'),
    path('results/<int:document_id>/', views.financial_results, name='financial_results'),
    path('list/', views.document_list, name='financial_list'),
]