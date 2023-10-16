from django.http import HttpResponse
from django.shortcuts import render

from .models import (
    ContactLink,
    ContactMessage,
    Friend,
    Presentation,
    Question,
    TitleText,
)

# Create your views here.
def index(request):
    main_text = TitleText.objects.get(pk=1)

    context = {"main_text": main_text}
    return render(request, "main/homepage.html", context)


def whoami(request):
    infos = Presentation.objects.get(pk=1)

    context = {"picture": infos.picture, "textEN": infos.textEN, "textFR": infos.textFR}
    return render(request, "main/whoami.html", context)


def faq(request):
    questions = Question.objects.all().order_by("pk")
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
