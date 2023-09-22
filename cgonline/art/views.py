from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
import random

from .models import Album, Piece

# Create your views here.
def art_galery(request):
    albums = Album.objects.all()
    content = []
    for album in albums:
        pieces = Piece.objects.filter(album=album)
        if pieces:
            content.append(tuple((album, random.choice(pieces))))
    context = {
        "content": content,
    }
    return render(request, "art/main_galery.html", context)


def album(request, album_url):
    album = get_object_or_404(Album, url=album_url)
    pieces = Piece.objects.filter(album=album)
    context = {
        "album": album,
        "pieces": pieces,
    }
    return render(request, "art/generic_galery.html", context)


def piece(request, album_url, piece_url):
    album = get_object_or_404(Album, url=album_url)
    piece = get_object_or_404(Piece, url=piece_url)
    context = {
        "album": album,
        "piece": piece,
    }
    return render(request, "art/generic_piece.html", context)


def latest(request):

    context = {
        "pieces": Piece.objects.all().order_by("-upload_date")[:6],
    }
    return render(request, "art/latest.html", context)


def art_random(request):
    piece = random.choice(Piece.objects.all())
    context = {
        "piece": random.choice(Piece.objects.all()),
        "album": piece.album,
    }
    return render(request, "art/generic_piece.html", context)
