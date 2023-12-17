from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'enter your username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'enter your email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'enter your firstname', 'autofocus': True}),
            'last_name': forms.TextInput(attrs={'placeholder': 'enter your lastname'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}),
        error_messages={'required': 'Username is required'}
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        error_messages={'required': 'Password is required'}
    )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets= {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your blog title'}),
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter your blog content....'})
        }