from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def dom(request):
    return render(request, 'users/home.html')


def home(request):
    return render(request, 'users/time_table.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'users/login.html', context)


def profile(request):
    return render(request, 'users/profile.html')


def logoutUser(request):
    logout(request)
    return redirect('dom')


def registerPage(request):
    if request.user.is_authenticated:
        redirect('home')
    else:
        form = UserRegisterForm()
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {username}')
                return redirect('login')

        return render(request, 'users/register.html', {'form': form})
