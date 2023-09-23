from django.urls import path

from . import views

urlpatterns = [
    path("", views.dev_main, name="dev_main"),
    path("latest", views.latest, name="latest"),
    path("random", views.art_random, name="random"),
    path("tag/<slug:tag>", views.search_tags, name="tags"),
    path("<slug:project_url>", views.project, name="project"),
]

app_name = "dev"
