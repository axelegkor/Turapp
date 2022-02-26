from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Hike
from .forms import HikeForm


# Create your views here.
def hike(request, pk):
    hike = Hike.objects.get(id=pk)
    participants = hike.participants.all()
    participantcount = hike.participants.all().count()
    context = {'hike': hike, 'participants': participants, 'participantcount': participantcount}
    return render(request, 'base/hike.html', context)

@login_required(login_url='login')
def createHike(request):
    form = HikeForm()

    if request.method == 'POST':
        form = HikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('overview')

    context = {'form': form}
    return render(request, 'base/createhike.html', context)

def updateHike(request, pk):
    hike = Hike.objects.get(id=pk)
    form = HikeForm(instance=hike)

    if request.user != hike.host:
        return HttpResponse('Du er ikke arrangør på denne turen og kan ikke endre den!')

    if request.method == 'POST':
        form = HikeForm(request.POST, instance=hike)
        if form.is_valid():
            form.save()
            return redirect('overview')

    context = {'form': form}
    return render(request, 'base/createhike.html', context)

@login_required(login_url='login')
def deleteHike(request,pk):
    hike = Hike.objects.get(id=pk)
    if request.method == 'POST':
        hike.delete()
        return redirect('overview')
    context = {'hike':hike}
    return render(request, 'base/deletehike.html', context)




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

@login_required(login_url='login')
def enrolled(request):
    hikes = Hike.objects.all()
    participants = Hike.participants
    context = {'hikes': hikes, 'participants': participants}
    return render(request, 'base/enrolled.html', context)

# login_required

@login_required(login_url='login')
def overview(request):
    hikes = Hike.objects.all()
    participants = Hike.participants
    context = {'hikes': hikes, 'participants': participants}
    return render(request, 'base/overview.html', context)

# @login_required

@login_required(login_url='login')
def mypage(request):
    return render(request, 'base/mypage.html')


def description(request):
    return render(request, 'base/description.html')


def home(request):
    hikes = Hike.objects.all()
    participants = Hike.participants
    context = {'hikes': hikes, 'participants': participants}
    return render(request, 'base/home.html', context,)


def about(request):
    return render(request, 'base/about.html')
