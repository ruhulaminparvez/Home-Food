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

from store.utils import cookieCart, cartData, guestOrder


def home(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    products = Product.objects.all()
    medium_banners = MediumBanner.objects.all()
    onsales = OnSale.objects.all()
    bestsellers = BestSeller.objects.all()
    topviews = TopView.objects.all()
    small_banners = SmallBanner.objects.all()

    context = {  
        'products': products, 'medium_banners': medium_banners, 'onsales': onsales, 'bestsellers': bestsellers, 'topviews': topviews, 'small_banners': small_banners, 'cartItems': cartItems, 'order': order, 'items': items  
        }

    return render(request, 'home.html', context)




def contact(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()

    context = {  
        'products': products, 'cartItems': cartItems, 'order': order, 'items': items  
        }

    return render(request, 'contact.html', context)



def service(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()

    context = {  
        'products': products, 'cartItems': cartItems, 'order': order, 'items': items  
        }

    return render(request, 'service.html', context)



def food(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()

    context = {  
        'products': products, 'cartItems': cartItems, 'order': order, 'items': items  
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
    return render(request, 'cart.html', context)



def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)
    


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


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)



    