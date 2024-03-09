from django.shortcuts import render
from .models import Salary

# Create your views here


def salary_list(request):
    salaries = Salary.objects.all()
    return render(request, 'payroll_management/salary_list.html', {'salaries': salaries})
