from django.urls import path

from . import views

urlpatterns = [
    path("", views.dev_main, name="dev_main"),
]

app_name = "dev"
