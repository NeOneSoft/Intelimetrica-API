# Djangorestframework
from rest_framework import serializers

# Models
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    """
    Restaurant general purpose serializer
    """

    class Meta:
        model = Restaurant
        fields = ('id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')


class CreateRestaurantSerializer(serializers.ModelSerializer):
    """
    Create Restaurant serializer
    """

    class Meta:
        model = Restaurant
        fields = ('id','rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')
