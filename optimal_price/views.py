from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView
import pickle
from optimal_price.models import User
# Create your views here.


class APIView(TemplateView):
    template_name = "home.html"

class APIListView(ListView):
    model = User