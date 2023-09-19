from django.http import HttpResponse
from django.shortcuts import render

from .models import ContactLink, ContactMessage, Friend, Presentation, Question

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
    questions = Question.objects.all()
    context = {
        "questions": questions,
    }
    return render(request, "main/faq.html", context)


def contact(request):
    msg = ContactMessage.objects.get(pk=1)
    links = ContactLink.objects.all()

    context = {
        "msg": msg,
        "links": links,
    }
    return render(request, "main/contact.html", context)


def friend(request):
    friends = Friend.objects.all()

    context = {
        "friends": friends,
    }
    return render(request, "main/friends.html", context)
