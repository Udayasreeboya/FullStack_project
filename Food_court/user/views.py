from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login

def signup(request):
    data = json.loads(request.body)

    username = data['username']
    password = data['password']

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "User already exists"})

    User.objects.create_user(username=username, password=password)

    return JsonResponse({"message": "Signup successful"})



def login_user(request):
    data = json.loads(request.body)

    username = data['username']
    password = data['password']

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"error": "Invalid credentials"})

    login(request, user)
    return JsonResponse({"message": "Login successful"})
def forgot_password(request):
    data = json.loads(request.body)

    username = data['username']
    new_password = data['new_password']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"})

    user.set_password(new_password)
    user.save()

    return JsonResponse({"message": "Password reset successful"})