from django.urls import path

from . import views

urlpatterns = [
    path("", views.art_galery, name="art_galery"),
    path("<slug:album>", views.album, name="art_album"),
    path("<slug:album>/<slug:piece>", views.piece, name="art_piece"),
]
