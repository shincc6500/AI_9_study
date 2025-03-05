# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.http import require_http_methods
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib import messages
from .forms import ProfileUpdateForm



def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("post:index")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "login.html", context)

@login_required
def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect("post:index")

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "signup.html", context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect("post:index")

@require_http_methods(["GET","POST"])
def update(request):
    
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect("post:index")
    else : 
        form = CustomUserChangeForm(instance=request.user)
    context = {"form" : form}
    return render(request, 'update.html', context)

def change_passward(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("post:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "change_passward.html", context)

@login_required
def profile(request):    
    context = {'user': request.user}
    return render(request, 'profile.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()            
            return redirect('users:profile')  # 프로필 페이지로 리디렉션
    else:
        form = ProfileUpdateForm(instance=request.user)
    context = {
        'form': form
        }
    return render(request, 'update_profile.html', )



