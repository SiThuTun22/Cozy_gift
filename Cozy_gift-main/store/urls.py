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
  path('rose/',views.rose,name="rose"),
  path('tulip/',views.tulip,name="tulip"),
  path('orchid/',views.orchid,name="orchid"),
  path('product/',views.products,name="product"),
  path('about-us/', views.about_us, name="about_us"),
  path('category/<str:foo>',views.category,name="category"),
  path('product-detail/<int:pk>',views.product_detail,name="product_detail"),
  path('flowerLanding/',views.flowerLanding,name="flowerLanding"),
  path('flower/<str:name>/', views.flower_detail, name='flower_detail'),
]
