from django.contrib import admin
from .models import SmallBanner

# Register your models here.
class SmallBannerAdmin(admin.ModelAdmin):
    list_display = ['s_tag', 's_headline', 's_span', 'slug', 's_image',  's_btn_text']
    prepopulated_fields = {'slug': ('s_tag',)}

admin.site.register(SmallBanner, SmallBannerAdmin)
