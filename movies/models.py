from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    year = models.DateField(help_text='Release year')
    genre = ArrayField(models.CharField(max_length=100))
    poster = models.CharField()