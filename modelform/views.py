from django.shortcuts import render
from modelform.forms import ProjectForm
from modelform.models import Project


# Create your views here.

def index(request):
    return render(request, 'templatesapp/home.html')


def listProjects(request):
    projectsList = Project.objects.all()
    return render(request, 'templatesapp/listprojects.html', {'project': projectsList})


def addproject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'templatesapp/addproject.html', {'form': form})
