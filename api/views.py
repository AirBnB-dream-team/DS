from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from api.serializers import AirbnbSerializer
from api.models import Airbnb
from django.views.generic import TemplateView, ListView
from rest_framework import serializers, viewsets
from rest_framework import generics


# Create your views here.

class APIView(TemplateView):
    template_name = "home.html"

class APIListView(ListView):
    model = Airbnb

class AirbnbList(generics.ListCreateAPIView):
    queryset = Airbnb.objects.all()
    serializer_class = AirbnbSerializer

class AirbnbDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airbnb.objects.all()
    serializer_class = AirbnbSerializer