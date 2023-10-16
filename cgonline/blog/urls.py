from django.urls import path

from . import views

urlpatterns = [
    path("", views.blog_main, name="blog_main"),
    path("tag/<slug:tag>", views.search_tags, name="tags"),
    path("<slug:entry_url>", views.blog_entry, name="entry"),
]

app_name = "blog"
