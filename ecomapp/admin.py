from django.contrib import admin
from ecomapp.models import category,product,Order,customer,cart
# Register your models here.
admin.site.register(category)
admin.site.register(product)
admin.site.register(Order)
admin.site.register(customer)
admin.site.register(cart)