from django.urls import path

from . import views

urlpatterns = [
    path("", views.art_galery, name="art_galery"),
    path("latest", views.latest, name="latest"),
    path("random", views.art_random, name="random"),
    path("<slug:album_url>", views.album, name="album"),
    path("<slug:album_url>/<slug:piece_url>", views.piece, name="piece"),
]

app_name = "art"
