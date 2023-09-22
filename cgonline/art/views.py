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
    pieces = Piece.objects.filter(album=album).order_by("-upload_date")
    context = {
        "album": album,
        "pieces": pieces,
    }
    return render(request, "art/generic_galery.html", context)


def piece(request, album_url, piece_url):
    album = get_object_or_404(Album, url=album_url)
    piece = get_object_or_404(Piece, url=piece_url)
    pieces = Piece.objects.filter(album=album).order_by("-upload_date")
    next = None
    prev = None
    i = 0
    max_length = len(pieces)
    for piece_ in pieces:
        if piece_ == piece:
            if i < max_length - 1:
                next = pieces[i + 1]
            else:
                next = pieces[0]
            if i > 0:
                prev = pieces[i - 1]
            else:
                prev = pieces[max_length - 1]
        i += 1
    context = {
        "album": album,
        "piece": piece,
        "next": next,
        "prev": prev,
        "is_random": False if max_length > 1 else True,
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
        "is_random": True,
    }
    return render(request, "art/generic_piece.html", context)
