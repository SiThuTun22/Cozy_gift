from django.contrib import admin
from .models import Category,Product,Profile,Customer,Order
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Customer)
admin.site.register(Order)

class ProfileInline(admin.StackedInline):
  model = Profile

class UserAdmin(admin.ModelAdmin):
  model = User
  field = ["username","first_name","last_name","email"]
  inlines = [ProfileInline]

# Unregister the old way
admin.site.unregister(User)

admin.site.register(User,UserAdmin)