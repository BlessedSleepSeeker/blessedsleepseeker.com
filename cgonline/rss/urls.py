from django.urls import path

from . import views

urlpatterns = [
    # path("", views.rss_feed, name="rss_all"),
    # path("latest", views.latest, name="latest"),
    # path("<slug:rssnews_pk>", views.rss_news, name="rss_news")
]

app_name = "rss"
