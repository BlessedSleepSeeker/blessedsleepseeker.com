from django.http import HttpResponse
from django.shortcuts import render

from .models import Presentation

# Create your views here.
def index(request):
    context = {}
    return render(request, "main/homepage.html", context)


def whoami(request):
    infos = Presentation.objects.get(pk=1)

    context = {"picture": infos.picture, "text": infos.textEN}
    print(infos.picture)
    return render(request, "main/whoami.html", context)


def faq(request):
    context = {}
    return render(request, "main/faq.html", context)


def contact(request):
    context = {}
    return render(request, "main/contact.html", context)


def friend(request):
    context = {}
    return render(request, "main/friends.html", context)
