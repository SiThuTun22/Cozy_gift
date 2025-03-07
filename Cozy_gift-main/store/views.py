from django.shortcuts import render,redirect
from .models import Product,Profile,Category,FlowerStories,Color
from .forms import SignUpForm, UpdateUserForm,ChangePasswordForm, UserInfoForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import json
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django.shortcuts import render, redirect
from django.shortcuts import redirect
# image according to month
from datetime import datetime
from django.template.loader import render_to_string

def home(request):
    current_month = datetime.now().strftime("%B")  # Get current month name (e.g., "March")

    context = {
        'products': Product.objects.all(),
        'current_month': current_month,  # Add this to context
    }
    language = request.session.get('language', 'eng')  # Default to English
    template_name = 'home_eng.html' if language == 'eng' else 'home_mm.html'
    return render(request, template_name, context)




def search(request):
  if request.method == "POST":
    searched = request.POST['searched']

    searched = Product.objects.filter(Q(name__icontains = searched) | Q(description__icontains = searched)) 
    if not searched:
      messages.success(request,"the product doesn't not exist. Please try again!")
      return render(request,"search.html",{})
    else:
      return render(request,"search.html",{"searched":searched})
  return render(request,"search.html",{})

 #coming
def coming_soon(request):
    return render(request, 'coming.html',{}) 

def update_info(request):
  if request.user.is_authenticated:
    # Get Current User
    current_user = Profile.objects.get(user__id=request.user.id)
    # Get Current User's Shipping Info
    shipping_user = ShippingAddress.objects.get(user__id=request.user.id)

    # Get Original User form
    form = UserInfoForm(request.POST or None,instance=current_user)

    # Get User's Shipping form
    shipping_form = ShippingForm(request.POST or None,instance = shipping_user)
    if form.is_valid() or shipping_form.is_valid():
      # Save original form
      form.save()
      # Save shipping_form
      shipping_form.save()
      messages.success(request,"Your Info Has Been Updated!!")
      return redirect('home')
    return render(request,"update_info.html",{'form':form,'shipping_form':shipping_form})
  else:
    messages.success(request,"You Must Be Logged In")
    return redirect('home')

def flower_detail(request, name):
    language = request.session.get('language', 'eng')
    template_name = f'{name}_{language}.html'
    
    return render(request, template_name)

def category(request,foo):
  # replace if there is dash
  foo = foo.replace('-',' ')
  # Grab the category from the url
  try:
    # Look up the category 
    language = request.session.get('language', 'eng')  # Default to English
    template_name = 'category_eng.html' if language == 'eng' else 'category_mm.html'
    category = Category.objects.get(name = foo)
    products = Product.objects.filter(category=category)
    return render(request, template_name,{'products':products,'category':category})
  except:
    return redirect('home')

def product_detail(request,pk):
  product_detail = Product.objects.get(id=pk)
  return render(request,"product_detail.html",{'product_detail':product_detail})

# About Us page view
def about_us(request):
    return render(request, 'about_us.html')

def filter_data(request):
  print("🔵 Received GET data:", request.GET)
  colors=request.GET.getlist('color[]')

  categories = request.GET.getlist('category[]')
  allProducts = Product.objects.all().distinct()
  if len(colors) > 0:
     allProducts = allProducts.filter(color_id__in=colors).distinct()
  if len(categories) > 0:
     allProducts = allProducts.filter(category_id__in=categories).distinct()

  # print("🟢 Extracted colors:", colors)
  # print("🟢 Filtered Products:", list(products.values()))
  t = render_to_string('product_list.html',{'data':allProducts})
  # print("Rendered Template:", t)
  return JsonResponse({'data':t})

def products(request):
  products = Product.objects.all()
  language = request.session.get('language', 'eng')  # Default to English
  template_name = 'product_eng.html' if language == 'eng' else 'product_mm.html'
  colors = Color.objects.all()
  categories = Category.objects.all()
  return render(request,template_name,{'products':products,'colors':colors,'categories':categories})

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                new_password = form.cleaned_data['new_password1']
                current_user.set_password(new_password)
                current_user.save()
                # Save plaintext password to profile
                profile = Profile.objects.get(user=current_user)
                profile.plaintext_password = new_password
                profile.save()
                messages.success(request, "Your Password Has Been Updated")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'update_password.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In")
        return redirect('home')

def update_user(request):
  if request.user.is_authenticated:
    current_user = User.objects.get(id=request.user.id)

    user_form = UpdateUserForm(request.POST or None,instance=current_user)
    if user_form.is_valid():
      user_form.save()
      login(request,current_user)
      messages.success(request,"User Has Been Updated!!")
      return redirect('home')
    return render(request,"update_user.html",{'user_form':user_form})
  else:
    messages.success(request,"You Must Be Logged In")
    return redirect('home')


def login_user(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      # Do some shopping cart stuff
      current_user = Profile.objects.get(user__id = request.user.id)
      # Get their saved cart from database
      saved_cart = current_user.old_cart
      # Convert database string to python dictionary
      if saved_cart:
        #  Convert to dictionary using JSON
        converted_cart = json.loads(saved_cart)
        # add the loaded cart dictionary to our session
        # Get the cart
        cart = Cart(request)
        # loop thru the cart and add the items from the database
        
        for key,value in converted_cart.items():
           cart.db_add(product=key,quantity=value)
           
      messages.success(request,('You have been logged in'))
      return redirect('home')
    else:
      messages.success(request,('There was an error,please try again'))
      return redirect('login')
  else:
    return render(request,'login.html',{})
def logout_user(request):
  logout(request)
  messages.success(request,("You have been logged out..."))
  return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            plaintext_password = form.cleaned_data['password1']
            # Log in user
            login(request, user)
            # Save plaintext password to profile
            profile = Profile.objects.get(user=user)
            profile.plaintext_password = plaintext_password
            profile.save()
            messages.success(request, ("Username Created! Please fill out the form."))
            return redirect('update_info')
        else:
            messages.success(request, ("Whoops! There was a problem Registering."))
            return redirect('register')
    return render(request, 'signup.html', {'form': form})
# rose twy upgrade code for mm font
def rose(request):
    language = request.session.get('language', 'eng')  # Default to English
    template_name = 'pages/rose_eng.html' if language == 'eng' else 'pages/rose_mm.html'
    return render(request, template_name)

def orchid(request):
    language = request.session.get('language', 'eng')  # Default to English
    template_name = 'pages/orchid_eng.html' if language == 'eng' else 'pages/orchid_mm.html'
    return render(request, template_name)

def tulip(request):
    language = request.session.get('language', 'eng')  # Default to English
    template_name = 'pages/tulip_eng.html' if language == 'eng' else 'pages/tulip_mm.html'
    return render(request, template_name)

def sunflower(request):
    language = request.session.get('language', 'eng')  # Default to English
    template_name = 'pages/sunflower_eng.html' if language == 'eng' else 'pages/sunflower_mm.html'
    return render(request, template_name)

def lotus(request):
    language = request.session.get('language', 'eng')  # Default to English
    template_name = 'pages/lotus_eng.html' if language == 'eng' else 'pages/lotus_mm.html'
    return render(request, template_name)

def daisy(request):
    language = request.session.get('language', 'eng')  # Default to English
    template_name = 'pages/daisy_eng.html' if language == 'eng' else 'pages/daisy_mm.html'
    return render(request, template_name)



# def flowerLanding(request):
#   flowers = FlowerStories.objects.all()
#   return render(request,"flowerlanding.html",{'flowers':flowers})



def flowerLanding(request):
    flowers = FlowerStories.objects.all()
    language = request.session.get('language', 'eng')  # Default to English
    template_name = 'flowerlanding_eng.html' if language == 'eng' else 'flowerlanding_mm.html'
    return render(request, template_name,{'flowers':flowers} )


# toggle also modify for mm font
def toggle_language(request):
    if request.session.get('language', 'eng') == 'eng':
        request.session['language'] = 'mm'
    else:
        request.session['language'] = 'eng'
    return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirect back to the previous page
