"""task_14 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from restaurants import views
from api.views import (RestaurantList, RestaurantDetail, RestaurantUpdate, RestaurantDelete, RestaurantCreate, Register)
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('restaurants/list/',views.restaurant_list ,name='restaurant-list'),
    path('restaurants/<int:restaurant_id>/detail/',views.restaurant_detail,name='restaurant-detail'),
    path('restaurants/create/',views.restaurant_create ,name='restaurant-create'),
    path('restaurants/<int:restaurant_id>/update/',views.restaurant_update ,name='restaurant-update'),
    path('restaurants/<int:restaurant_id>/delete/',views.restaurant_delete ,name='restaurant-delete'),
    path('restaurants/favorite/',views.favorite_restaurants ,name='favorite-restaurant'),

    path('restaurants/<int:restaurant_id>/favorite/',views.restaurant_favorite ,name='restaurant-favorite'),
    path('restaurants/<int:restaurant_id>/item/add/',views.item_create ,name='item-create'),
    path('signup/',views.signup ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),
    path('no-access/',views.no_access ,name='no-access'),

    path('api/list', RestaurantList.as_view(), name='list'),
    path('api/<int:restaurant_id>/update/', RestaurantUpdate.as_view(), name='update'),
    path('api/<int:restaurant_id>/delete/', RestaurantDelete.as_view(), name='delete'),
    path('api/<int:restaurant_id>/', RestaurantDetail.as_view(), name='detail'),
    path('api/create/', RestaurantCreate.as_view(), name='create'),
    path('api/login/', obtain_jwt_token),
    path('api/register/', Register.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)