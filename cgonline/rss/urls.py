from django.urls import path

from .feeds import RssFeed

from . import views

urlpatterns = [
    path("", views.rss_pres, name="rss_pres"),
    path("feed", RssFeed(), name="rss_feed"),
]

app_name = "rss"
