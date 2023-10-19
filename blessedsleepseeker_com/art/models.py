import datetime
import os
from django.db import models
from django.utils import timezone

# Create your models here.
class Piece(models.Model):
    name = models.CharField(max_length=2000)
    nameFR = models.CharField(max_length=2000)
    url = models.CharField(max_length=200, unique=True)
    upload_date = models.DateTimeField(default=timezone.now)
    authors = models.TextField()
    comment = models.TextField(blank=True, help_text="Optional")
    commentFR = models.TextField(blank=True, help_text="Optional")
    file = models.ImageField(upload_to="upload/art/")
    source_file = models.FileField(upload_to="upload/art/sources/")
    album = models.ForeignKey("Album", on_delete=models.CASCADE)

    scale_algorithm = [
        ("auto", "auto"),
        ("crisp-edges", "crisp-edges"),
        ("smooth", "smooth"),
        ("pixelated", "pixelated"),
    ]

    scaling_method = models.CharField(
        max_length=20, choices=scale_algorithm, default="pixelated"
    )

    @property
    def was_published_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=7)

    @property
    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension[1:]

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=2000)
    nameFR = models.CharField(max_length=2000)
    url = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, help_text="Optional")
    descriptionFR = models.TextField(blank=True, help_text="Optional")

    @property
    def was_published_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=7)

    def __str__(self):
        return self.name
