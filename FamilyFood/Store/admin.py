from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(TrendingItem)
admin.site.register(HotItem)
admin.site.register(SmallBanner)