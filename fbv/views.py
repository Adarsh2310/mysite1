from django.shortcuts import render
from django.http import HttpResponse
from fbv.models import Student


# Create your views here.
def getstudents(request):
    student = Student.objects.all()
    return render(request, 'templatesapp/fbv.html', {'student': student})
