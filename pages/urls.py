from django.urls import path
from pages.views import home, about, contact, services

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
]
