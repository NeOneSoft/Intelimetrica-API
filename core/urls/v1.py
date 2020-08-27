#Django
from django.conf.urls import url, include

#Djangorestframework
from rest_framework import routers

#Views
from restaurants.views import RestaurantViewSet


#API urls
router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]