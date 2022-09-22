from django.db import models

# Create your models here.
class Performance(models.Model):
    cost  =models.IntegerField()
    revenue = models.IntegerField()
    creation_date = models.DateTimeField()
    # profit =