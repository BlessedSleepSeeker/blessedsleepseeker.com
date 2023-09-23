import random
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.utils import timezone

from .models import Project

PROJECT_PER_PAGE = 12

# Create your views here.
def dev_main(request):
    projs = Project.objects.filter(visible_starting__lt=timezone.now())
    paginator = Paginator(projs, PROJECT_PER_PAGE)

    page_nbr = request.GET.get("page")
    page_obj = paginator.get_page(page_nbr)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "dev/main.html", context)


def project(request, project_url):
    article = get_object_or_404(Project, url=project_url)
    if not article.should_display():  # means it's not ready to be uploaded
        raise Http404("Article should not be visible")
    template_url = "dev/" + project_url + ".html"
    context = {}
    return render(request, [template_url, "404.html"], context)


def latest(request):
    context = {
        "projects": Project.objects.filter(
            visible_starting__lt=timezone.now()
        ).order_by("-upload_date")[:PROJECT_PER_PAGE],
    }
    return render(request, "art/latest.html", context)


def art_random(request):
    project = random.choice(Project.objects.filter(visible_starting__lt=timezone.now()))
    context = {
        "project": random.choice(Project.objects.all()),
        "album": project.album,
        "is_random": True,
    }
    return render(request, "art/generic_project.html", context)


def search_tags(request, tag):
    projs = Project.objects.filter(
        tags__contains=tag, visible_starting__lt=timezone.now()
    ).order_by("-upload_date")
    paginator = Paginator(projs, PROJECT_PER_PAGE)

    page_nbr = request.GET.get("page")
    page_obj = paginator.get_page(page_nbr)

    context = {
        "page_obj": page_obj,
        "tag": tag,
    }
    return render(request, "dev/main.html", context)
