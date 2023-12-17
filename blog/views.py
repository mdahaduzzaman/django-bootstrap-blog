from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Post
from .forms import *
import json
# Home page
def home(request):
    posts = Post.objects.all()
    for post in posts:
        print(post.likedBy.all())
    return render(request, 'blog/home.html', {'posts': posts})

def getLike(request):
    if request.method == "POST":
        data = json.loads(request.body)

        post_id = data.get('postId')
        choice = data.get('liked')
        
        if post_id:
            try:
                post = Post.objects.get(pk=post_id)
                if request.user.is_authenticated:
                    user = request.user
                    if choice:
                        if user in post.likedBy.all():
                            post.likedBy.remove(user)  # Remove the user from likedBy if already liked
                        else:
                            post.likedBy.add(user)  # Add the user to likedBy if not already liked                       
                    else:
                        if user in post.dislikedBy.all():
                            post.dislikedBy.remove(user)  # Remove the user from likedBy if already liked
                        else:
                            post.dislikedBy.add(user)  # Add the user to likedBy if not already liked
                    return JsonResponse({'like': post.likedBy.all().count(), 'dislike': post.dislikedBy.all().count(), 'postId': post_id })
                else:
                    return JsonResponse({'error': "You aren't authenticated. Please login first"}, status=401)
            except Post.DoesNotExist:
                return JsonResponse({'error': 'Post not found'}, status=404)
        else:
            return JsonResponse({'error': 'Invalid request'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

# About page
def about(request):
    return render(request, 'blog/about.html')
    
# Contact page
def contact(request):
    return render(request, 'blog/contact.html')


# Dashboard page
def dashboard(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, "Post published successfully")
            return redirect('dashboard')
    else:
        form = PostForm()
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/dashboard.html', {'posts': posts, 'form': form})

def editPost(request, postID):
    post = None
    try:
        post = Post.objects.get(pk=postID)
    except Exception as e:
        messages.error(request, "Post isn't available.")
        return redirect('dashboard')
    else:
        if post.author != request.user:
            messages.error(request, "You don't have the right to modify this post.")
            return redirect('dashboard')
        
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'post updated successfully.')
            return redirect('dashboard')
    else:
        form = PostForm(instance=post)
    posts = Post.objects.all()
    return render(request, 'blog/dashboard.html', {'posts': posts, 'form': form})

# Login page
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})
    
# Signup page
def signup_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created Successfully.")
            if user is not None:
                login(request, user=user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'blog/signup.html', {'form': form})
    
def logout_user(request):
    logout(request)
    messages.warning(request, 'logged Out Successfully!')
    return redirect('home')

