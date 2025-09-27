from django.urls import path
from Main import views

urlpatterns = [
    path('dashboard' , views.dashboard ,name='dashboard'),
]