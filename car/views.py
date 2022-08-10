from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Brand
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BrandForm
from django.contrib.auth.decorators import login_required

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
    brands = Brand.objects.all()
    context = {
        'brands':brands
    }
    return render(request, 'cars/brand.html', context)

def create_brand(request):
    if request.method == 'POST':
        brand_name = request.POST['brand']
        if brand_name:
            brand = Brand(brand_name=brand_name)
            brand.save()
            return redirect('brand')       
    context = {
        
    }
    return render(request, 'cars/brand.html', context)



@login_required
def brand_update(request,id):
    brand = get_object_or_404(Brand,id=id)
    form = BrandForm(request.POST or None , instance= brand)
    if request.method == 'POST':
        form = BrandForm(request.POST or None , instance= brand)
        if form.is_valid():
            form.save()
            brand_update = f'You have update {brand.brand_name} brand'
            # messages.error(request,brand_update)
            return redirect('brand')
        else:
          form = BrandForm(request.POST)  
          
    context = {
        'brand':brand,
        'form':form
    }
    return render(request, 'cars/brand_update.html', context)



def delete_brand(request, id):
    brand = Brand.objects.get(id=id)
    brand.delete()
    return redirect('brand')