from django.shortcuts import render
from django.contrib.syndication.views import Feed
from django.urls import reverse

from cgonline.blog.models import Article

# Create your views here.


class RssFeed(Feed):
    title = "All news from Camille Gouneau"
    link = ""
    description = "There's news !"

    def items(self):
        return Article.objects.all().order_by("-pub_date")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse("rss_news", args=[item.pk])


class Latest(Feed):
    title = "News from Camille Gouneau"
    link = "latest_news"
    description = "There's news !"

    def items(self):
        return Article.objects.all().order_by("-pub_date")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse("rss_news", args=[item.pk])


class RssNews(Feed):
    title = "News from Camille Gouneau"
    link = "specific_news"
    description = "There's news !"

    def items(self):
        return RssNews.objects.all().order_by("-pub_date")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse("rss_news", args=[item.pk])
