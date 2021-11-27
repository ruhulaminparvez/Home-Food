from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime

from .models import *


def home(request):
    trendingitems = TrendingItem.objects.all()
    context = {'trendingitems': trendingitems}

    return render(request, 'home.html', context)

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog-single-sidebar.html')


def small_banner(request):
    smallbanners = SmallBanner.objects.all()
    context = {'smallbanners': smallbanners}

    return render(request, 'small-banner.html', context)





