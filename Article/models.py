from django.conf import settings
from django.db import models
from Users.models import User
from django.contrib.postgres.fields import ArrayField

class Article(models.Model):

    GENRES = [("rent", "rent"),("sale", "sale")]



    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='articles', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()
    #image = models.CharField(max_length= 1000)
    images = ArrayField(models.CharField(max_length=1000), blank=True, null=True)
    type = models.CharField(max_length=30, blank=False, choices=GENRES, default="rent")


    def __str__(self):
        return '%s (%f)' % (self.title, self.price)