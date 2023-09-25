from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template

from .models import ProjectInfos

# Create your views here.
def index(request):
    projs = ProjectInfos.objects.all()

    context = {
        "projs": projs,
    }
    return render(request, "special/main.html", context)


def project(request, project_url):
    to_render = "special/" + project_url + ".html"

    context = {}
    return render(request, [to_render, "404.html"], context)
