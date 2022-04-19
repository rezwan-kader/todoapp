from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User, auth


# from UsersApp.models import UserAccount


def index(request):
    return render(request, 'index.html')


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'index.html')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Credentials! Email/User doesn't exist!")
            return redirect('index')
    else:
        return redirect('index')


def account(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username Taken!")
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email Taken!")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account Created! Log in to Get Started!")
            return redirect('index')
        return redirect('index')

    else:
        return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('index')
