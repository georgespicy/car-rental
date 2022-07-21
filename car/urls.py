from django.urls import path
from .views import toyota

urlpatterns = [
    path('', toyota, name='toyota')
]
