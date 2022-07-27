from django.urls import path
from .views import car, search, brand

urlpatterns = [
    path('', car, name='car'),
    path('search', search, name='search'),
    path('brand', brand, name='brand'),
]
