from django.contrib import admin

from watch_web.models import Brand
from watch_web.models import Product
from watch_web.models import Review


admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Review)