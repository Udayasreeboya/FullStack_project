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
            return redirect('/menu/')
        else:
            return render(request, 'auth/login.html', {"error": "Invalid credentials"})

    return render(request, 'auth/login.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        return redirect('/login/')

    return render(request, 'auth/signup.html')


def forgot_password(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()

        return redirect('/login/')

    return render(request, 'auth/forgot.html')