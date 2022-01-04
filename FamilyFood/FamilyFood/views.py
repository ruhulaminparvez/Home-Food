from django.shortcuts import render
from django.http import HttpResponse
from store.models import *
from medium_banner.models import *
from lower_card.models import *
from small_banner.models import *
from django.contrib.auth.forms import UserCreationForm


def home(request):
    products = Product.objects.all()
    medium_banners = MediumBanner.objects.all()
    onsales = OnSale.objects.all()
    bestsellers = BestSeller.objects.all()
    topviews = TopView.objects.all()
    small_banners = SmallBanner.objects.all()

    context = {  
        'products': products, 'medium_banners': medium_banners, 'onsales': onsales, 'bestsellers': bestsellers, 'topviews': topviews, 'small_banners': small_banners  
        }

    return render(request, 'home.html', context)


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


def service(request):
    return render(request, 'service.html')

def food(request):
    products = Product.objects.all()

    context = {  
        'products': products  
        }

    return render(request, 'foods.html', context)

def login_registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            
    context = {'form': form}
    return render(request, 'login-registration.html')
