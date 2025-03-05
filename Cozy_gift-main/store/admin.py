from django.contrib import admin
from .models import Category, Product, Profile, Customer, Order, FlowerStories, Flower_Categories,Color
from django.contrib.auth.models import User

# Register your models
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Flower_Categories)
admin.site.register(FlowerStories)
admin.site.register(Color)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address1', 'city', 'state', 'country', 'plaintext_password')
    search_fields = ('user__username', 'phone', 'address1', 'city')
    list_filter = ('state', 'country')

admin.site.register(Profile, ProfileAdmin)

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]

# Unregister the old User admin and register the modified one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
