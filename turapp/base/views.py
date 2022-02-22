from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username) # sjekker om brukeren finnes
        except:
            messages.error(request, "Brukeren eksisterer ikke.")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) # dette lager en session i browseren, bruker er logget inn i databasen
            return redirect('home')
        else:
            messages.error(request, "Brukernavn eller passord eksisterer ikke.")

    context={}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'base/home.html')