# Create your models here.
from django.db import models


class Employee(models.Model):
    empNo = models.IntegerField()
    empName = models.CharField(max_length=100)
    empSalary = models.IntegerField()
    empAddress = models.CharField(max_length=200)

