from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('some', some, name='some'),
    path('get-like', getLike, name='getlike'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('dashboard', dashboard, name='dashboard'),
    path('edit-post/<int:postID>', editPost, name='editPost'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('signup', signup_user, name='signup'),
]
