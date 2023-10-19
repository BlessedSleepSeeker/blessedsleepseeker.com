from datetime import timezone
from django.db import models
from django.urls import reverse


class RssEmail(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
