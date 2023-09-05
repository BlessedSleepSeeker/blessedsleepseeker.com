from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def dev_main(request):
    return HttpResponse("dev")
