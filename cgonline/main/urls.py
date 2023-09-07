from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("whoaim", views.whoami, name="whoami"),
    path("faq", views.faq, name="faq"),
    path("contact", views.contact, name="contact"),
]

app_name = "main"
