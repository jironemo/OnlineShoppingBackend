from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .services.user import UserService
from shop.models import Cart,CartProducts
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserService.create_cart(user)
            login(request, user)
            return redirect('/shop/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if(not request.GET.get('next')):
                    
                    return redirect('/shop/')
                else:
                    return redirect(request.GET.get('next'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def cart_view(request):
    if request.user:
        cart = Cart.objects.filter(user=request.user)[0]
        cart_products = CartProducts.objects.filter(cart=cart)
        return render(request,'cart.html',{'cart':cart_products})
        
def logout_view(request):
    logout(request)
    return redirect('login')
