from django.shortcuts import render, HttpResponse, redirect
from .models import *

def projects(request):
    return render(request, "projects/projects.html")

def project(request, prid):
    context = {
        'proj': Project.objects.get(id=prid)
    }
    return render(request, "projects/project.html", context)

def conservation(request):
    return render(request, "projects/conservation.html")