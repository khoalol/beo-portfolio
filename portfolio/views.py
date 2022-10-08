from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.
def home(request):
    projects = Project.objects.all()
    parameters = {'projects':projects}
    return render(request, 'portfolio/home.html', parameters)
