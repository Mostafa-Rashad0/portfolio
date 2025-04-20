from django.shortcuts import render
from .models import Project,Category
def projects(request):
    projects = Project.objects.all()
    return render(request,'projects/projects.html',{'projects':projects})

def eachproject(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request,'projects/eachproject.html',{'project':project})
