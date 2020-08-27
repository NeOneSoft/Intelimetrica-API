# Djangorestframework
from rest_framework import viewsets

# Models
from .models import Restaurant

# Serializers
from .serializers import RestaurantSerializer, CreateRestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    Restaurant (EndPoint)
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    # Overwrite our get serializer class
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateRestaurantSerializer
        return RestaurantSerializer
