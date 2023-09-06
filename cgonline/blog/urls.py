from django.urls import path

from . import views

urlpatterns = [
    path("", views.blog_main, name="blog_main"),
]

app_name = "blog"
