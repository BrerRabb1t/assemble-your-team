from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse

from user.forms import ProfileForm, UserLoginForm, UserRegistrationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'Welcome back, {username}')
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title': "Log in",
        'form': form
    }
    return render(request, "user/login.html", context)
    

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'Recived 50$ Gift')
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': "Sign In",
        'form': form
    }
    return render(request, "user/registration.html", context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': "Profile",
        'form': form
    }
    return render(request, "user/profile.html", context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))


def cart(request, product_id):
    if request.user.is_authenticated:
        if product_id == 3:
            messages.success(request, f'Email me: kirsanov.pashenka@gmail.com')
        else:
            messages.warning(request, f'Not enough money')
    else:
        return redirect(reverse('user:login'))

    return redirect(reverse('main:index'))
