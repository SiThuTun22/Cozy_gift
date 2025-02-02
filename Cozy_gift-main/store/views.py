from django.shortcuts import render,redirect
from .models import Product,Profile,Category,FlowerStories
from .forms import SignUpForm, UpdateUserForm,ChangePasswordForm, UserInfoForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Create your views here.
 #coming
def coming_soon(request):
    return render(request, 'coming.html',{}) 

def update_info(request):
  if request.user.is_authenticated:
    current_user = Profile.objects.get(user__id=request.user.id)

    form = UserInfoForm(request.POST or None,instance=current_user)
    if form.is_valid():
      form.save()
      messages.success(request,"Your Info Has Been Updated!!")
      return redirect('home')
    return render(request,"update_info.html",{'form':form})
  else:
    messages.success(request,"You Must Be Logged In")
    return redirect('home')
def flowerLanding(request):
  flowers = FlowerStories.objects.all()
  return render(request,"flowerlanding.html",{'flowers':flowers})

def flower_detail(request,name):
  return render(request, f'{name}.html')

def category(request,foo):
  # replace if there is dash
  foo = foo.replace('-',' ')
  # Grab the category from the url
  try:
    # Look up the category 
    category = Category.objects.get(name = foo)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html',{'products':products,'category':category})
  except:
    return redirect('home')

def product_detail(request,pk):
  product_detail = Product.objects.get(id=pk)
  return render(request,"product_detail.html",{'product_detail':product_detail})

# About Us page view
def about_us(request):
    return render(request, 'about_us.html')

def products(request):
  products = Product.objects.all()
  return render(request,'product.html',{'products':products})

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

def rose(request):
  return render(request,"rose.html",{})

def tulip(request):
  return render(request,"tulip.html",{})

def orchid(request):
  return render(request,"orchid.html",{})

def home(request):
  products = Product.objects.all()
  return render(request,'home.html',{'products':products})
def login_user(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
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
