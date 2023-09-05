from django.urls import path

from . import views

urlpatterns = [
    path("", views.diy_main, name="diy_main"),
]
