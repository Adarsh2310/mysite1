from django.db import models

# Creaprintte your models here.

class Employeedetails(models.Model):
    fir_nm=models.CharField(max_length=30)
    ls_nm=models.CharField(max_length=30)
    sal=models.FloatField()
