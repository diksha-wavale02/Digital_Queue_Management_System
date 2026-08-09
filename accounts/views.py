from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                username=username,
                password=password
            )

            if user:

                login(request, user)

                return redirect('dashboard')

    else:

        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):

    logout(request)

    return redirect('login')


def dashboard(request):

    return render(request, 'accounts/dashboard.html')