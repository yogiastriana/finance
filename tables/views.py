from django.shortcuts import render
from .models import CompanyData
from . import views

def table_view(request):
    data = CompanyData.objects.all()  # Ambil data dari database
    context = {
        'run_data': {
            'input_data': {
                'ticker_data': data
            }
        }
    }
    return render(request, 'tables/table.html', context)
