from django.shortcuts import render
from projects.models import Project

# Create your views here.


def project_list(request):
    project_list = Project.objects.all()
    context = {
        "projects": project_list,
    }
    return render(request, "projects/list.html", context)