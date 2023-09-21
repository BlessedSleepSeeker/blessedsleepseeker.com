from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="special_main"),
    path("<slug:project_url>", views.project, name="special_project"),
]

app_name = "special"
