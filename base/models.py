from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=120)
    image_link = models.TextField()
    desc_short = models.CharField(max_length=200)
    desc_long = models.TextField()
    is_proper = models.BooleanField()
    datetime = models.CharField(max_length=120)