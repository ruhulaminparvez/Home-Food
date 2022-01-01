from django.shortcuts import render
from django.http import HttpResponse
from store.models import *
from django.contrib.auth.forms import UserCreationForm


def home(request):
    products = Product.objects.all()

    context = {  
        'products': products  
        }

    return render(request, 'home.html', context)

def medium_banner(request):
    medium_banner = MediumBanner.objects.all()

    context = {  
        'medium_banner': medium_banner  
        }

    return render(request, 'medium-banner.html', context)


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def login_registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            
    context = {'form': form}
    return render(request, 'login-registration.html')
