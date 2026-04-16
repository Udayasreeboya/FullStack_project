from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/cart/')   # after login go to cart
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid credentials'})

    return render(request, 'auth/login.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            return render(request, 'auth/signup.html', {'error': 'Passwords not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'auth/signup.html', {'error': 'User already exists'})

        User.objects.create_user(username=username, email=email, password=password)

        return redirect('/auth/login/')

    return render(request, 'auth/signup.html')


def forgot_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            return render(request, 'auth/forgot.html')

        try:
            user = User.objects.get(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect('/auth/login/')
        except User.DoesNotExist:
            return render(request, 'auth/forgot.html', {'error': 'User not found'})

    return render(request, 'auth/forgot.html')