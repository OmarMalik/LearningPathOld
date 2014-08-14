from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

class Track(models.Model):
	name = models.CharField(max_length=128, unique=True)

class Page(models.Model):
    track = models.ForeignKey(Track)
    title = models.CharField(max_length=128)
    url = models.URLField()
    position = models.IntegerField()

