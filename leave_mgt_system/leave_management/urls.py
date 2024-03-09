from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('leave_list/', views.leave_list, name='leave_list'),
    # Other URL patterns...
]
