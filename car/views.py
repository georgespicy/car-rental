from django.shortcuts import render, redirect
from .models import Car, Brand
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BrandForm

# Create your views here.


def car(request):
    cars = Car.objects.all()
    p = Paginator(cars, 2)
    page = request.GET.get('page')
    car_Pages = p.get_page(page)

    context = {
        'cars': car_Pages,
    }
    return render(request, 'cars/car.html', context)

# =============================CAR================================

def search(request):
    cars = Car.objects.order_by('created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(car_name__icontains=keyword)
    context = {
        'cars': cars
    }
    return render(request, 'cars/search.html', context)

# ===========================search=================================

def brand(request):
    brand = Brand.objects.all()
    context = {
        'brand':brand
    }
    return render(request, 'cars/brand.html', context)

def create_brand(request):
    if request.method == 'POST':
        brandform = BrandForm(request.POST or None)
        if brandform.is_valid():
            brandform.save()
            return redirect('brand')
        else: 
            brandform = BrandForm()
    context = {
        'brandform': brandform
    }
    return render(request, 'cars/brand.html', context)