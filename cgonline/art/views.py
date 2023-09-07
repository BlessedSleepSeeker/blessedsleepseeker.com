from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def art_galery(request):
    context = {}
    return render(request, "art/main_galery.html", context)


def album(request, album):
    context = {}
    return render(request, "art/generic_galery.html", context)


def piece(request, album, piece):
    context = {}
    return render(request, "art/generic_piece.html", context)
