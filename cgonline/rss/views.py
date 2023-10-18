from django.shortcuts import render

# Create your views here.
def rss_pres(request):
    context = {}
    return render(request, "rss/rss_pres.html", context)
