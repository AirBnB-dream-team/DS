from django.db import models

# Create your models here.
class Airbnb(models.Model):
    id = models.IntegerField(primary_key=True)
    zipcode = models.TextField(default='')
    bathrooms = models.TextField(default='')
    bedrooms = models.TextField(default='')
    optimal = models.IntegerField(default=0)