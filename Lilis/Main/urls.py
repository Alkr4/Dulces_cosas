from django.urls import path
from Main import views
from Main.views import products_view

urlpatterns = [
    path('dashboard' , views.dashboard ,name='dashboard'),
    path('products' , products_view ,name='products'),
]