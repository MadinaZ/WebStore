from django.contrib import admin
from .models import Product
from .models import Offer

class ProductAdmin(admin.ModelAdmin): #inherits all the common functionalities
    list_display = ('name', 'price', 'stock')#columns that should be visible

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

# Registering your 'products' in the admin section(blue page)
admin.site.register(Product, ProductAdmin) #site means object itself
admin.site.register(Offer,OfferAdmin)