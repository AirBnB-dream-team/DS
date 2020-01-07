from rest_framework import serializers
from api.models import Airbnb

class AirbnbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airbnb
        fields = [
            'bedrooms',
            'bathrooms',
            'zipcode',
        ]