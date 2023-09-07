from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def diy_main(request):
    context = {}
    return render(request, "diy/main.html", context)
