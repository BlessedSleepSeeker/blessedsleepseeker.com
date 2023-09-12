from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.whoami, name="whoami"),
    path("faq", views.faq, name="faq"),
    path("contact", views.contact, name="contact"),
    path("friends", views.friend, name="friends"),
]

app_name = "main"
