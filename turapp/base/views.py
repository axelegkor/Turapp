from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # sjekker om brukeren finnes
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Brukeren eksisterer ikke.")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # dette lager en session i browseren, bruker er logget inn i databasen
            login(request, user)
            return redirect('home')
        else:
            messages.error(
                request, "Brukernavn eller passord eksisterer ikke.")

    context = {}
    return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/register.html', {'form': form})

# log_required


def enrolled(request):
    return render(request, 'base/enrolled.html')

# login_required


def overview(request):
    return render(request, 'base/overview.html')

# @login_required


def mypage(request):
    return render(request, 'base/mypage.html')


def description(request):
    return render(request, 'base/description.html')


def home(request):
    return render(request, 'base/home.html')


def about(request):
    return render(request, 'base/about.html')
