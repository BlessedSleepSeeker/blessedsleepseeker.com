from django.db import models

# Create your models here.
class Question(models.Model):
    questionEN = models.CharField(max_length=2000)
    answerEN = models.TextField()
    questionFR = models.CharField(max_length=2000)
    answerFR = models.TextField()
    picture = models.ImageField(upload_to="upload/questions/", blank=True)

    def __str__(self):
        return self.questionEN


class Friend(models.Model):
    name = models.CharField(max_length=2000)
    picture = models.ImageField(upload_to="upload/friends/", blank=True)
    link = models.URLField(max_length=2000, blank=True)
    short_descriptionEN = models.CharField(max_length=2000, blank=True)
    short_descriptionFR = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.name


class ContactOption(models.Model):
    email = models.EmailField(max_length=2000, blank=True)
    twitter = models.URLField(max_length=2000, blank=True)
    instagram = models.URLField(max_length=2000, blank=True)
    discord = models.URLField(max_length=2000, blank=True)


class Presentation(models.Model):
    textFR = models.TextField()
    textEN = models.TextField()
    picture = models.ImageField(upload_to="upload/aboutme/", blank=True)
