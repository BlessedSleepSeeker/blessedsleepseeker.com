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

    name = models.CharField(max_length=2000)
    short_description = models.TextField(blank=True)
    vignette = models.ImageField(blank=True)
    upload_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)
    tags = models.TextField(blank=True, validators=[validate_tags])
    authors = models.TextField()

    languages = models.CharField(max_length=200)
    active = models.BooleanField(default=False)

    source = models.FileField(upload_to="dev/")
