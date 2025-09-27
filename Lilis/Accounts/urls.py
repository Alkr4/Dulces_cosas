from django.urls import path
from Accounts import views
from django.contrib.auth import views as views_auth

urlpatterns = [
    path('login/', views_auth.LoginView.as_view(),name='login'),
    path('logout/', views_auth.LogoutView.as_view(),name='logout'),
    path('registro/', views.registro,name='registro')    
]