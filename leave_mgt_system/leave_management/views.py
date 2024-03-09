from django.shortcuts import render
from .models import Leave

# Create your views here.


def leave_list(request):
    leaves = Leave.objects.all()
    return render(request, 'leave_management/leave_list.html', {'leaves': leaves})
