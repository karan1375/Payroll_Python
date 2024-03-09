from django.db import models

# Create your models here.


class Salary(models.Model):
    employee = models.ForeignKey('leave_management.Employee', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()
