from django.urls import path
from .views import car, delete_brand, search, brand, create_brand

urlpatterns = [
    path('', car, name='car'),
    path('search', search, name='search'),
    path('brand', brand, name='brand'),
    path('create_brand', create_brand, name='create_brand'),
    path('delete_brand/<int:id>', delete_brand, name='delete_brand'),
]