from django.urls import path
from rest_framework import routers
from optimal_price.views import APIView

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'SaltyUsers', SaltyUserViewSet)

urlpatterns = [
    path('home/', APIView.as_view(), name='home'),
]