from django.shortcuts import render
from .models import Car

# Create your views here.

def toyota(request):
    cars = Car.objects.all()
    context = {
        'cars': cars,
    }
    return render (request, 'cars/toyota.html', context)