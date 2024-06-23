
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()
def login(request):
    print('salve')
    return render(request, 'login.html')

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def home(request):
    return render(request, 'home.html', {'user': request.user})