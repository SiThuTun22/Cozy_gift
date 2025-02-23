from django.contrib import admin
from .models import ShippingAddress,Order,OrderItem
# Register your models here.
# Register the model on the admin section
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
