from django.db import models

# Create your models here.
class FAQuestion(models.Model):
    question = models.CharField(max_length=2000)
    answer = models.TextField()
    picture = models.ImageField(upload_to="questions/", blank=True)


class Friend(models.Model):
    name = models.CharField(max_length=2000)
    picture = models.ImageField(upload_to="friends/", blank=True)
    link = models.URLField(max_length=2000, blank=True)


class ContactOption(models.Model):
    email = models.EmailField(max_length=2000, blank=True)
    twitter = models.URLField(max_length=2000, blank=True)
    instagram = models.URLField(max_length=2000, blank=True)
    discord = models.URLField(max_length=2000, blank=True)
