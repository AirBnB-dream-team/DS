from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render
from api.serializers import AirbnbSerializer
from api.models import Airbnb
from django.views.generic import TemplateView, ListView
from rest_framework import serializers, viewsets
from rest_framework import generics


# Create your views here

"""
TODO
I need to return something in post reposne. 
"""
def post(request):
    if request.method == POST:
        data = {
            'here' : 'there'
        }
    return JsonResponse(data, safe=True)