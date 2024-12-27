from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
  path('',views.home,name="home"),
  path('signup',views.register_user,name="register"),
  path('login/',views.login_user,name='login'),
  path('logout/',views.logout_user,name="logout"),
  path('update_user/',views.update_user,name="update_user"),
  path('update_password/',views.update_password,name="update_password"),
  path('discovery/',views.discovery,name="discovery"),
  path('product/',views.products,name="product"),
]
