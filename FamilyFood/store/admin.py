from django.contrib import admin
from .models import Product, MediumBanner

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'image', 'image_hover', 'slug', 'tag_class', 'tag']
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)

class MediumBannerAdmin(admin.ModelAdmin):
    list_display = ['m_image', 'm_tag', 'm_headline', 'm_btn_text']
    prepopulated_fields = {'slug': ('m_headline',)}

admin.site.register(MediumBanner, MediumBannerAdmin)