from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "main/homepage.html", context)


def whoami(request):
    context = {}
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
