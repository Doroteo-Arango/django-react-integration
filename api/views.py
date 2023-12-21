from django.shortcuts import render

import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

@require_POST
def login_view(request):
    # Parse user data from JSON body
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    
    # Check if username & password exists
    if username is None or password is None:
        return JsonResponse({"detail":"Please provide correct username and/or password"})
    
    # Authenticate user
    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse({"detail":"Invalid credentials"}, status=400)
    
    login(request, user)
    return JsonResponse({"detail":"Successful login"})

def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"detail":"You are not logged in"}, status=400)
    logout(request)
    return JsonResponse({"detail":"Successful logout"})
    
@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"isAuthenticated": False})
    return JsonResponse({"isAuthenitcated": True})

def whoami_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"isAuthenticated": False})
    return JsonResponse({"username":request.user.username})