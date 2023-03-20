from django.contrib import admin
from firstapp.models import Employeedetails


# Register your models here

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['fir_nm', "ls_nm", "sal"]


admin.site.register(Employeedetails,EmployeeAdmin)
