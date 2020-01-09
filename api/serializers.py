from rest_framework import serializers
from api.models import Airbnb

class AirbnbSerializer(serializers.ModelSerializer):
        bedrooms = serializers.IntegerField()
        bathrooms = serializers.IntegerField()
        zipcode = serializers.IntegerField()
        optimal = serializers.IntegerField()