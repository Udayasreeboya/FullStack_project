from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/cart/')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid credentials'})

    return render(request, 'auth/login.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password != confirm:
            return render(request, 'auth/signup.html', {'error': 'Passwords not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'auth/signup.html', {'error': 'User already exists'})

        User.objects.create_user(username=username, email=email, password=password)

        return redirect('/auth/login/')

    return render(request, 'auth/signup.html')


def forgot_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password != confirm:
            return render(request, 'auth/forgot.html', {'error': 'Passwords not match'})

        try:
            user = User.objects.get(username=username, email=email)
        except User.DoesNotExist:
            return render(request, 'auth/forgot.html', {'error': 'User not found'})

        user.set_password(password)
        user.save()

        return redirect('/auth/login/')

    return render(request, 'auth/forgot.html')