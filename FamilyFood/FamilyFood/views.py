from django.shortcuts import render
from django.http import HttpResponse
from store.models import *



def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {  
        'products': products  
        }

    return render(request, 'home.html', context)

def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')