from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, ProductForm
from .models import Product

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Home View
def home_view(request):
    return render(request, 'inventApp/home.html')

############### CRUD = CREATE, READ, UPDATE, DELETE ####################
################# CRUD = CODE Start ####################################

# Create View
@login_required(login_url='login')
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'inventApp/product_form.html', {'form': form})

# Read View
@login_required(login_url='login')
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'inventApp/product_list.html', {'products': products})

# Update View
@login_required(login_url='login')
def product_update_view(request, product_id):
   product = Product.objects.get(product_id=product_id)
   form = ProductForm(instance=product)
   if request.method == 'POST':
       form = ProductForm(request.POST, instance=product)
       if form.is_valid():
           form.save()
           return redirect('product_list')
   return render(request, 'inventApp/product_form.html', {'form': form})

# Delete View
@login_required(login_url='login')
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventApp/product_confirm_delete.html', {'product': product})

################# CRUD = CODE COMPLETE ##################################

##################### START - User Register/Authentication ######################
# Register a user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!!")
            return redirect("login")

    context = {'form': form}
    return render(request, 'inventApp/register.html', context)

# login view
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context ={'form': form}
    return render(request, 'inventApp/login.html', context)

# Dashboard view
@login_required(login_url='login')
def dashboard(request):
    return render(request, "inventApp/dashboard.html")

# User Logout
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout success!!")
    return redirect("login")

##################### END - User Register/Authentication ######################