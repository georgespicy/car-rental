from django.urls import path
from .views import car, delete_brand, search, brand

urlpatterns = [
    path('', car, name='car'),
    path('search', search, name='search'),
    path('brand', brand, name='brand'),
    path('delete-_brand/<int:id>', delete_brand, name='delete_brand'),
]