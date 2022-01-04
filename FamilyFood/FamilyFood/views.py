from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import datetime

from store.models import *
from medium_banner.models import *
from lower_card.models import *
from small_banner.models import *
from django.contrib.auth.forms import UserCreationForm

from .utils import cookieCart, cartData, guestOrder


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




def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html')



def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html')
    


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)




    