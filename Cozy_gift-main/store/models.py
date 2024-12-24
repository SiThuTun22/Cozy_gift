from django.db import models
from django.contrib.auth.models import User

# Categories
class Category(models.Model):
  name = models.CharField(max_length = 50)
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = 'categories'

# Create your models here.
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
  
  def __str__(self):
    return self.user.username
  
# Create a user profile by default when user signs up
def create_profile(sender,instance,created,**kwargs):
  if created:
    user_profile = Profile(user=instance)
    user_profile.save()
    
class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(default=0,decimal_places = 2,max_digits = 6)
  category = models.ForeignKey(Category,on_delete = models.CASCADE,default=1)
  description = models.CharField(max_length=250,default='',blank=True,null = True) 
  image = models.ImageField(upload_to = 'uploads/product/')
  is_sale = models.BooleanField(default =False)
  sale_price = models.DecimalField(default=0,decimal_places=2,max_digits=6)
  def __str__(self):
    return self.name

