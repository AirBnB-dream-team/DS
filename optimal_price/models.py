from django.db import models

# Create your models here.

class User(models.Model):
    bedrooms = models.IntegerField() 
    bathrooms = models.IntegerField() 
    minimum_nights = models.IntegerField()
    zipcode = models.IntegerField()
    host_neighbourhood = models.TextField()
    property_type = models.TextField()
    room_type = models.TextField()
    optimal_price = models.IntegerField()