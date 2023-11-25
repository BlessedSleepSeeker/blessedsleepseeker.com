from django.http import HttpResponse, FileResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from PIL import Image
import random, io

from .models import Album, Piece

ITEM_PER_PAGE = 6
# Create your views here.
def art_galery(request):
    all_albums = Album.objects.all().order_by("-creation_date")
    paginator = Paginator(all_albums, ITEM_PER_PAGE)

    page_nbr = request.GET.get("page")
    page_obj = paginator.get_page(page_nbr)
    content = []
    for album in page_obj:
        pieces = Piece.objects.filter(album=album)
        if pieces:
            content.append(tuple((album, random.choice(pieces))))
    context = {
        "page_obj": page_obj,
        "content": content,
    }
    return render(request, "art/main_galery.html", context)


def album(request, album_url):
    album = get_object_or_404(Album, url=album_url)
    pieces = Piece.objects.filter(album=album).order_by("-upload_date")
    paginator = Paginator(pieces, ITEM_PER_PAGE)

    page_nbr = request.GET.get("page")
    page_obj = paginator.get_page(page_nbr)
    context = {
        "album": album,
        "page_obj": page_obj,
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


def scaled_piece_download(request, album_url, piece_url, size):
    if size <= 0 or size > 2000:
        return HttpResponse("Error : Size must be between 1 and 2000")
    album = get_object_or_404(Album, url=album_url)
    piece = get_object_or_404(Piece, album=album, url=piece_url)

    sent_piece = io.BytesIO()
    with Image.open(piece.file) as new_piece:
        w, h = new_piece.size
        resized = new_piece.resize(
            [int((w * size) / 100), int((h * size) / 100)],
            resample=Image.Resampling.NEAREST,
        )
        resized.save(sent_piece, "png")

    return HttpResponse(
        sent_piece.getvalue(),
        headers={
            "Content-Type": "image/png",
            "Content-Disposition": f'attachment; filename="{piece.name}_{size}"',
        },
    )


def latest(request):

    context = {
        "pieces": Piece.objects.all().order_by("-upload_date")[:6],
    }
    return render(request, "art/latest.html", context)


def art_random(request):
    piece = random.choice(Piece.objects.all())
    context = {
        "piece": piece,
        "album": piece.album,
        "is_random": True,
    }
    return render(request, "art/generic_piece.html", context)
