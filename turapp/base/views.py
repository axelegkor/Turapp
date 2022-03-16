from importlib.resources import contents
from multiprocessing import context

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import HikeForm, RegisterForm, UserCreationForm
from .models import Hike


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


@login_required(login_url='login')
def signupHike(request, pk):
    hike = Hike.objects.get(id=pk)
    hike.joinHike(request.user)
    context = {'hike': hike}
    return render(request, 'base/signuphike.html', context)

@login_required(login_url='login')
def signoffHike(request, pk):
    hike = Hike.objects.get(id=pk)
    hike.dropHike(request.user)
    context = {'hike': hike}
    return render(request, 'base/signoffhike.html', context)


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
    if request.user.is_anonymous:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                form.save() 
                new_user = authenticate(username=username, password=password)
                if new_user is not None:
                    login(request, new_user)
                    return redirect("home")
    else:
        return redirect("logoutUser")
            
    form = RegisterForm()
    
    context ={
        "form":form
        }
    return render(request, 'base/register.html', context)

    
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
    user = request.user
    hikes = Hike.objects.all()
    participants = Hike.participants
    context = {'hikes': hikes, 'participants': participants, 'user': user}
    return render(request, 'base/home.html', context,)


def about(request):
    return render(request, 'base/about.html')
