from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def art_galery(request):
    return HttpResponse("artgalery")


def album(request, album):
    return HttpResponse(album)


def piece(request, album, piece):
    return HttpResponse(album + piece)
