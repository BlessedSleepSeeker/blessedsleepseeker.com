from django.shortcuts import render
from django.contrib.syndication.views import Feed
from django.urls import reverse, reverse_lazy

from blog.models import Article

# Create your views here.


class RssFeed(Feed):
    title = "Blessed Sleep Seeker's Blog"
    link = "/blog/"
    description = "There's news !"

    def items(self):
        return Article.objects.all().order_by("-visible_starting")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.short_descriptionEN

    def item_link(self, item):
        return reverse_lazy("blog:entry", args=[item.short_title])


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
