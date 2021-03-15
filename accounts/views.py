from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponse

# Create your views here.
 
 
def signup(request):
    try:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            user = User.objects.create_user(
                username = username,
                email = email,
                password = password2
            ).save()
            return redirect('login')
    except:
        pass
    return render(request, 'accounts/signup.html')


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request, username = username, password = password)
    if user:
        login(request, user)
        return redirect('home')
    else:
        redirect('login')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')