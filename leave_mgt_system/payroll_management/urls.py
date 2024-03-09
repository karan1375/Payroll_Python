from django.urls import path
from . views import salary_list

urlpatterns = [
    path('salary-list/', salary_list, name='salary-list.html'),
]
