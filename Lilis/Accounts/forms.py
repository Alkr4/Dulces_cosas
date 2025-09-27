from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='email',
        widget=forms.EmailInput(attrs={'placeholder': 'email@email.cl'})
        )
    first_name = forms.CharField(
        required=True,
        max_length=30,
        label='nombre', 
        widget=forms.TextInput(attrs={'placeholder': 'Nombre'})
        )
    last_name = forms.CharField(
        required=True,
        max_length=30,
        label='apellido',
        widget=forms.TextInput(attrs={'placeholder': 'Apellido'})
        )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {campo: "" for campo in fields} 

