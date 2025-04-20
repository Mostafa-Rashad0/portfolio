from django.shortcuts import render
from projects.models import Project

def home(request):
    # Get the latest 3 projects
    projects = Project.objects.all().order_by('-upload_date')[:3]
    return render(request, 'page/home.html', {'projects': projects})


