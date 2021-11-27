from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="blog"),
    path('small-banner/', views.small_banner, name="small-banner"),
]