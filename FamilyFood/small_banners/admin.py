from django.contrib import admin
from .models import SmallBanner

# Register your models here.
class SmallBannerAdmin(admin.ModelAdmin):
    list_display = ['small_banner_sub_heading', 'small_banner_heading', 'small_banner_btn_heading', 'small_banner_btn_url', 'small_banner_img', 'slug']
    prepopulated_fields = {'slug': ('small_banner_heading',)}

admin.site.register(SmallBanner, SmallBannerAdmin)