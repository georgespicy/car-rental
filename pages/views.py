from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import formcontact

# Create your views here.

def home(request):
    context = {}
    return render (request, 'pages/home.html', context)

def about(request):
    context = {}
    return render (request, 'pages/about.html', context)

def contact(request):
        # contactform = formcontact(request.POST or None)
    if request.method == 'POST':
        contactform = formcontact(request.POST or None)
        if contactform.is_valid():
            contactform.save()
            return redirect('home')
    else:
        contactform = formcontact()
    context = {
        'contactform' : contactform
    }
    return render (request, 'pages/contact.html', context)

def services(request):
    context = {}
    return render (request, 'pages/services.html', context)