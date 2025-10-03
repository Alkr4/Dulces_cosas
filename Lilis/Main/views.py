from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from Accounts.forms import RegistroForm
from Products.views import product

@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')

def products_view(request):
    products = product()
    return render(request, 'main/products.html', {'products': products})