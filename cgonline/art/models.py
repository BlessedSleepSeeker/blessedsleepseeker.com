import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Piece(models.Model):
    name = models.CharField(max_length=2000)
    upload_date = models.DateTimeField(default=timezone.now)
    authors = models.TextField()
    comment = models.TextField(blank=True, help_text="Optional")
    file = models.ImageField(upload_to="art/")
    album = models.ForeignKey("Album", on_delete=models.CASCADE)

    @property
    def was_published_recently(self):
        return self.visible_starting >= timezone.now() - datetime.timedelta(days=14)


class Album(models.Model):
    name = models.CharField(max_length=2000)
    creation_date = models.DateTimeField(default=timezone.now)
    vignette = models.ImageField(upload_to="art/", blank=True)
    description = models.TextField(blank=True, help_text="Optional")

    @property
    def was_published_recently(self):
        return self.visible_starting >= timezone.now() - datetime.timedelta(days=14)
