# import_data/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('ue/', views.upload_excel_file, name='upload_excel_file'),
]
