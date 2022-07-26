from django.shortcuts import render
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def toyota(request):
    cars = Car.objects.all()
    p = Paginator(cars, 2)
    page = request.GET.get('page')
    car_Pages = p.get_page(page)
    
    context = {
        'cars': car_Pages,
    }
    return render (request, 'cars/toyota.html', context)