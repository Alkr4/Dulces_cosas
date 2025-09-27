from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from Accounts.forms import RegistroForm

@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')

