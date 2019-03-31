from rest_framework import serializers
from restaurants.models import Restaurant, Item
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True) # extra creating the token manually
    class Meta:
        model = User
        fields = ['username', 'password', 'token']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER # extra creating the token manually
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)
        validated_data['token']=token
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'is_staff']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RestaurantListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = "detail",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
    )
    update = serializers.HyperlinkedIdentityField(
        view_name = "update",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
    )
    delete = serializers.HyperlinkedIdentityField(
        view_name = "delete",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
    )
    items = serializers.SerializerMethodField()
    item_set = ItemSerializer(many=True)

    owner = UserSerializer()

    class Meta:
        model = Restaurant
        fields = ['id', 'owner', 'name', 'opening_time', 'closing_time', 'detail', 'update', 'delete','items', 'item_set']
      
    def get_items(self, obj):
        items = obj.item_set.all()
        return ItemSerializer(items, many=True).data

class RestaurantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'opening_time', 'closing_time', ]
