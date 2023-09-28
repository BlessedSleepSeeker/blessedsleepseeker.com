from django.db import models

# Create your models here.
class ProjectInfos(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    descriptionEN = models.TextField()
    descriptionFR = models.TextField()
    picture = models.ImageField(upload_to="upload/aboutme/", blank=True)

    def __str__(self):
        return self.name
