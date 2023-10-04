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


class ContactMessage(models.Model):
    messageEN = models.TextField()
    messageFR = models.TextField()

    def __str__(self):
        return self.messageEN


class ContactLink(models.Model):
    title = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    direct_link = models.CharField(max_length=2000)
    comment = models.TextField(max_length=2000)
    commentFR = models.TextField(max_length=2000)
    emphasis = models.BooleanField()

    def __str__(self):
        return self.title


class Presentation(models.Model):
    textFR = models.TextField()
    textEN = models.TextField()
    picture = models.ImageField(upload_to="upload/aboutme/", blank=True)


class TitleText(models.Model):
    textEN = models.TextField()
    textFR = models.TextField()

    def __str__(self):
        return self.textEN
