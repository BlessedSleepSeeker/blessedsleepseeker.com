from django.shortcuts import render
from django.contrib.syndication.views import Feed
from django.urls import reverse, reverse_lazy
from django.utils.feedgenerator import Enclosure, RssFeed

from blog.models import Article
from art.models import Piece
from dev.models import Project as DevProject
from diy.models import Project as DIYProject

# Create your views here.


class BlogFeed(Feed):
    title = "Blessed Sleep Seeker's Blog"
    link = "/blog/"
    description = "Latest Blog Posts !"

    def items(self):
        return Article.objects.all().order_by("-visible_starting")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.short_descriptionEN

    def item_link(self, item):
        return reverse_lazy("blog:entry", args=[item.short_title])


class ArtFeed(Feed):
    title = "Blessed Sleep Seeker's Art"
    link = "/art/"
    description = "Latest Upload Pieces !"

    def get_object(self, request, *args, **kwargs):
        self.request = request
        return super(ArtFeed, self).get_object(request, *args, **kwargs)

    def items(self):
        return Piece.objects.all().order_by("-upload_date")[:2]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.comment if item.comment else ""

    def item_link(self, item):
        return reverse_lazy("art:piece", args=[item.album.url, item.url])

    def build_absolute_link(self, item):
        return self.request.build_absolute_uri(self.item_link(item))

    def item_enclosures(self, item):
        return [
            Enclosure(
                self.build_absolute_link(item),
                str(item.file.size),
                f"image/{item.file.name.split('.')[-1]}",
            )
        ]


class DevFeed(Feed):
    title = "Blessed Sleep Seeker's Dev Projects"
    link = "/dev/"
    description = "Latest Updated Dev Projects !"

    def items(self):
        return DevProject.objects.all().order_by("-update_date")[:2]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.short_description

    def item_link(self, item):
        return reverse_lazy("dev:project", args=[item.url])


class DIYFeed(Feed):
    title = "Blessed Sleep Seeker's DIY Projects"
    link = "/diy/"
    description = "Latest Updated DIY Projects !"

    def items(self):
        return DIYProject.objects.all().order_by("-update_date")[:2]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.short_description

    def item_link(self, item):
        return reverse_lazy("diy:project", args=[item.url])
