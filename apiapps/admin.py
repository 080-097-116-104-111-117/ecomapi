from django.contrib import admin
from . models import product
from .models import customer
from .models import order
from .models import ProductCategory


admin.site.register(product)
admin.site.register(customer)
admin.site.register(order)
admin.site.register(ProductCategory)
