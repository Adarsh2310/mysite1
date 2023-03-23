from django.db import models


# Create your models here.
class Project(models.Model):
    startdate = models.DateField()
    enddate = models.DateField()
    name = models.CharField(max_length=30)
    assigned_to = models.CharField(max_length=40)
    priority = models.IntegerField()
