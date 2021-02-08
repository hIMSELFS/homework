from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length = 16,label='Логин',widget=forms.TextInput(
        attrs={
            'class': 'form-control login',
            'autocomplete':'off'}
                )
            )
    password1 = forms.CharField(max_length = 32,label='Пароль',widget=forms.PasswordInput(
        attrs={'class': 'form-control login','autocomplete':'off'}
                )
            )
    password2 = forms.CharField(max_length=32, label='Повторите пароль',widget=forms.PasswordInput(
        attrs={
            'class': 'form-control login'}
                )
            )
    email = forms.EmailField(label='E-mail',widget=forms.EmailInput(
        attrs={
            'class': 'form-control login','autocomplete':'off'}
                )
            )

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=16, label='Логин', widget=forms.TextInput(
        attrs={
            'class': 'form-control login ',
            'autocomplete': 'off'}
    )
                               )
    password = forms.CharField(max_length=32, label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control login', 'autocomplete': 'off'}
    )
                                )
