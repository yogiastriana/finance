from django.urls import path
from .views import finance_dashboard_view

urlpatterns = [
    path('dashboard/', finance_dashboard_view, name='finance_dashboard'),
]
