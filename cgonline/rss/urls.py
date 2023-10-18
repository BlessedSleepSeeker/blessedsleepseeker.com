from django.urls import path

from .feeds import BlogFeed, ArtFeed, DevFeed, DIYFeed

from . import views

urlpatterns = [
    path("", views.rss_pres, name="rss_pres"),
    path("blog", BlogFeed(), name="blog_feed"),
    path("art", ArtFeed(), name="art_feed"),
    path("dev", DevFeed(), name="dev_feed"),
    path("diy", DIYFeed(), name="diy_feed"),
]

app_name = "rss"
