from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog_main(request):
    return HttpResponse("blog")
