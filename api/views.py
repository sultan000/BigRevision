from .models import Restaurant
from rest_framework.generics import ListAPIView
from api.models import Restaurant
from .Serializer import RestaurantListSerializer

# Complete me! I should be your APIListView


class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
