from django.contrib import admin
from .models import OnSale, BestSeller, TopView
# Register your models here.
class OnSaleAdmin(admin.ModelAdmin):
    list_display = ['os_headline', 'slug', 'os_image', 'os_price']
    prepopulated_fields = {'slug': ('os_headline',)}

admin.site.register(OnSale, OnSaleAdmin)


class BestSellerAdmin(admin.ModelAdmin):
    list_display = ['bs_headline', 'slug', 'bs_image', 'bs_price']
    prepopulated_fields = {'slug': ('bs_headline',)}

admin.site.register(BestSeller, BestSellerAdmin)


class TopViewAdmin(admin.ModelAdmin):
    list_display = ['tv_headline', 'slug', 'tv_image', 'tv_price']
    prepopulated_fields = {'slug': ('tv_headline',)}

admin.site.register(TopView, TopViewAdmin)