from datetime import date
from django.conf import settings
from django.db import models
from Users.models import User

class Reclamation(models.Model):
    Rec_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reclamations', on_delete=models.CASCADE)
    object = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField()
    Rec_for = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reclamations_for', on_delete=models.CASCADE)


    def __str__(self):
        return '%s --> %s' % (self.Rec_owner, self.Rec_for)