from django.urls import path, include
from . import views
from rest_framework import routers
from api.views import APIListView, APIView, AirbnbDetail, AirbnbList

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'SaltyUsers', SaltyUserViewSet)

urlpatterns = [
    path('home/', views.APIView.as_view(), name='home'),
    path('list/', views.APIListView.as_view(), name='api_list'),
    path('airbnb/', views.AirbnbList.as_view()),
    path('airbnb/<int:pk>/', views.AirbnbDetail.as_view()),
]