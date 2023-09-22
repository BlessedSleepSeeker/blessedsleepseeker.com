from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import Article

ITEM_PER_PAGE = 10

# Create your views here.
def blog_main(request):
    articles = Article.objects.all().order_by("-upload_date")
    paginator = Paginator(articles, ITEM_PER_PAGE)

    page_nbr = request.GET.get("page")
    page_obj = paginator.get_page(page_nbr)

    print(page_obj.paginator.num_pages)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "blog/main.html", context)


def blog_entry(request, entry_url):
    context = {
        "article": get_object_or_404(Article, short_title=entry_url),
    }
    return render(request, "blog/main.html", context)


def search_tags(request, tag):
    articles = Article.objects.filter(tags__contains=tag).order_by("-upload_date")
    paginator = Paginator(articles, ITEM_PER_PAGE)

    page_nbr = request.GET.get("page")
    page_obj = paginator.get_page(page_nbr)

    context = {
        "page_obj": page_obj,
        "tag": tag,
    }
    return render(request, "blog/main.html", context)
