from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView,

)
from restaurants.models import Restaurant
from .Serializer import (
    RestaurantListSerializer,
    RestaurantDetailSerializer,
    RestaurantCreateUpdateSerializer,
    RegisterSerializer,
)
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwner



class Register(CreateAPIView):
    serializer_class = RegisterSerializer
    
class RestaurantList(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    permission_class = [AllowAny,]
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['name', 'owner__username'] 
    # search through the object by username 

class RestaurantDetail(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'
    permission_class = [AllowAny,]

class RestaurantUpdate(RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'
    permission_class = [IsOwner,]

class RestaurantDelete(DestroyAPIView):
    queryset = Restaurant.objects.all()
    # serializer_class = RestaurantCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'
    permission_class = [IsAdminUser,]

class RestaurantCreate(DestroyAPIView):
    serializer_class = RestaurantCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
