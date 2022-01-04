from django.contrib import admin
from .models import MediumBanner

# Register your models here.
class MediumBannerAdmin(admin.ModelAdmin):
    list_display = ['m_headline', 'm_image', 'm_tag',  'm_btn_text']
    prepopulated_fields = {'slug': ('m_headline',)}

admin.site.register(MediumBanner, MediumBannerAdmin)