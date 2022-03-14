from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def dom(request):
    return render(request, 'users/home.html')


def home(request):
    return render(request, 'users/time_table.html')


def loginPage(request):
    return render(request, 'users/login.html')


def profile(request):
    # if request.method == 'POST':

    return render(request, 'users/profile.html')


def registerPage(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
