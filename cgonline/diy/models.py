import datetime
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Project(models.Model):
    def validate_tags(value):
        if " " in value:
            raise ValidationError(
                _(
                    "Les tags ne doivent pas avoir d'espace, et il ne doit y avoir qu'une virgule entre les tags"
                ),
                params={"value": value},
            )

    title = models.CharField(max_length=2000)
    url = models.CharField(max_length=200, unique=True)
    short_description = models.TextField()
    miniature = models.ImageField(upload_to="upload/dev/")
    tags = models.TextField(blank=True, validators=[validate_tags])

    # a project is only accessible when the datetime is past visible_starting
    visible_starting = models.DateTimeField(default=timezone.now)
    upload_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    authors = models.TextField()

    active_developpement = models.BooleanField(default=False)

    release = models.FileField(upload_to="upload/dev/releases/", blank=True)
    source = models.FileField(upload_to="upload/dev/sources/", blank=True)

    def should_display(self):
        return True if self.visible_starting <= timezone.now() else False

    @property
    def was_published_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=7)

    @property
    def was_updated_recently(self):
        return self.update_date >= timezone.now() - datetime.timedelta(days=7)

    @property
    def tags_formated(self):
        if self.tags:
            t = self.tags.rstrip(
                ","
            )  # remove special character ',' at the end to avoid empty tags bug
            return list(t.split(","))
        return []

    def __str__(self):
        return self.title
