from django.db import models

# Create your models here.
class Data(models.Model):
    exp = models.IntegerField()
    sal = models.IntegerField()