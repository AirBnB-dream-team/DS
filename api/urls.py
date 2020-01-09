from django.urls import path, include
from . import views
from rest_framework import routers
from api.views import APIListView, APIView, AirbnbDetail, AirbnbList


urlpatterns = [
    path('home/', views.APIView.as_view(), name='home'),
    path('list/', views.APIListView.as_view(), name='api_list'),
    path('airbnb/', views.AirbnbList.as_view()),
    path('airbnb/<int:pk>/', views.AirbnbDetail.as_view()),
]