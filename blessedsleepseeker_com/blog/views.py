from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.utils import timezone

import os

from .models import Article

ITEM_PER_PAGE = 10

# Create your views here.
def blog_main(request):
    all_articles = Article.objects.filter(visible_starting__lt=timezone.now()).order_by(
        "-visible_starting"
    )
    paginator = Paginator(all_articles, ITEM_PER_PAGE)

    page_nbr = request.GET.get("page")
    page_obj = paginator.get_page(page_nbr)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "blog/main.html", context)


def blog_entry(request, entry_url):
    article = get_object_or_404(Article, short_title=entry_url)
    if not article.should_display():  # means it's not ready to be uploaded
        raise Http404("Article should not be visible")
    template_url = "blog/articles/" + article.short_title + ".html"
    context = {
        "article": article,
    }
    if os.path.exists(template_url):
        return render(request, [template_url, "404.html"], context)
    
    return render(request, "blog/article.html", context)


def search_tags(request, tag):
    articles = Article.objects.filter(
        tags__contains=tag, visible_starting__lt=timezone.now()
    ).order_by("-visible_starting")
    paginator = Paginator(articles, ITEM_PER_PAGE)

    page_nbr = request.GET.get("page")
    page_obj = paginator.get_page(page_nbr)

    context = {
        "page_obj": page_obj,
        "tag": tag,
    }
    return render(request, "blog/main.html", context)
