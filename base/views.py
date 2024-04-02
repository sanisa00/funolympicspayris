from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.db.models import Q
from .models import Event, Topic, User

from django.contrib.auth import authenticate, login, logout

from .forms import UserForm, MyUserCreationForm


# Create your views here.

# events = [
#     {'id': 1, 'name': 'Ice Skating'},
#     {'id': 2, 'name': 'Rollerblading'},
#     {'id': 3, 'name': 'Aerobics'},
# ]

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
      
        try:
            user = User.objects.get(email=email)
           
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, email=email, password=password)
      

        if user is not None:
            login(request, user)
            return redirect('event')
        else:
            messages.error(request, 'Please login with your correct credential.')

    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, '   An error occured during registration!')

    return render(request, 'base/login_register.html', {'form': form})


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    topics = Topic.objects.all()
    context = {'user': user, 'topics': topics}
    return render(request, 'base/profile.html', context)


def home(request):
    return render(request, 'base/home.html')

@login_required(login_url='/login')
def event(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    events = Event.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q)|
        Q(description__icontains=q) 
        )

    topics = Topic.objects.all()
    event_count = events.count()

    context = {'events': events, 'topics': topics, 'event_count': event_count}
    return render(request, 'base/event.html', context)


@login_required(login_url='/login')
def livestream(request, pk):
    event = Event.objects.get(id=pk)
    topics = Topic.objects.all()
    events = Event.objects.all()

    context = {'event': event, 'topics': topics, 'events': events}
    return render(request, 'base/livestream.html', context)


def schedule(request):
    return render(request, 'base/schedule.html')

def about(request):
    return render(request, 'base/about.html')


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('update-user')

    return render(request, 'base/update-user.html', {'form':form})
    