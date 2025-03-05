from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Categories
class Category(models.Model):
  name = models.CharField(max_length = 50)
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = 'categories'

class Flower_Categories(models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
    return self.name
  class Meta:
    verbose_name_plural = "Flower categories"


class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  date_modified = models.DateTimeField(User,auto_now=True)
  phone = models.CharField(max_length=20,blank=True)
  address1 = models.CharField(max_length=200,blank=True)
  address2 = models.CharField(max_length=200,blank=True)
  city = models.CharField(max_length=200,blank=True)
  state = models.CharField(max_length=200,blank=True)
  zipcode = models.CharField(max_length=200,blank=True)
  country = models.CharField(max_length=200,blank=True)
  plaintext_password = models.CharField(max_length=128, blank=True, null=True)  # Add this field
  old_cart = models.CharField(max_length=200,blank=True,null=True)
  def __str__(self):
    return self.user.username
  
# Create a user profile by default when user signs up
def create_profile(sender,instance,created,**kwargs):
  if created:
    user_profile = Profile(user=instance)
    user_profile.save()

post_save.connect(create_profile,sender=User)
# Customer
class Customer(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  phone = models.CharField(max_length=10)
  email = models.EmailField(max_length=100)
  password = models.CharField(max_length=100)
  def __str__(self):
    return f'{self.first_name} {self.last_name}'
  
class Color(models.Model):
  title = models.CharField(max_length=100)
  color_code = models.CharField(max_length=100)
  def __str__(self):
    return self.title

class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.PositiveIntegerField(default=0)
  category = models.ForeignKey(Category,on_delete = models.CASCADE,null=True, blank=True)
  color = models.ForeignKey(Color,null=True, blank=True,on_delete=models.CASCADE)
  description = models.CharField(max_length=250,default='',blank=True,null = True) 
  image = models.ImageField(upload_to = 'uploads/product/')
  is_sale = models.BooleanField(default =False)
  sale_price = models.DecimalField(default=0,decimal_places=2,max_digits=6)
  def __str__(self):
    return self.name

class FlowerStories(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/flower/')
    category = models.ForeignKey(Flower_Categories, on_delete=models.CASCADE,null=True, blank=True)
    class Meta:
        verbose_name_plural = "Flower Stories"
    
    def __str__(self):
        return self.name


class Order(models.Model):
  product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True, blank=True)
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True, blank=True)
  quantity = models.IntegerField(default=1)
  address = models.CharField(max_length=100,default = '',blank = True)
  phone =  models.CharField(max_length=20,default='',blank=True)
  date = models.DateField(default=datetime.date.today)
  status = models.BooleanField(default = False)
  def __str__(self):
    return self.product

