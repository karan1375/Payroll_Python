from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=255)


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    is_approved = models.BooleanField(default=False)
