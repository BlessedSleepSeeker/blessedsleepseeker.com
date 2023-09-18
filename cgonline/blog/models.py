import datetime
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Article(models.Model):

    LANGUAGE_CHOICES = [
        ("FR", _("Francais")),
        ("EN", _("English")),
    ]

    title = models.CharField(max_length=200)
    # used for url creation, do not put maj char, space or special characters in it
    short_title = models.CharField(max_length=30, unique=True)
    vignette = models.ImageField(upload_to="upload/blog", null=True, blank=True)

    def validate_tags(value):
        if " " in value:
            raise ValidationError(
                _(
                    "Les tags ne doivent pas avoir d'espace, et il ne doit y avoir qu'une virgule entre les tags"
                ),
                params={"value": value},
            )

    tags = models.TextField(blank=True, validators=[validate_tags])

    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)

    # an inactive article isn't accessible and return a 404 when searched directly
    active = models.BooleanField(default=True)
    # an article is only accessible when the datetime is past visible_starting
    visible_starting = models.DateTimeField(default=timezone.now)
    upload_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    body = models.TextField(blank=True)

    def is_active(self):
        return self.active

    def should_display(self):
        return True if self.visible_starting <= timezone.now() else False

    @property
    def was_published_recently(self):
        return self.visible_starting >= timezone.now() - datetime.timedelta(days=14)

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
