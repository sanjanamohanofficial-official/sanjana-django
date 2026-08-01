from django.shortcuts import render, redirect
from .models import Player
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Home page view
def home(request):
    return render(request, 'players/home.html')


# Task 4 - Add a new player
def add_player(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        name          = request.POST.get('name')
        jersey_number = request.POST.get('jersey_number')
        position      = request.POST.get('position')
        team          = request.POST.get('team')

        p = Player()
        p.user          = request.user
        p.name          = name
        p.jersey_number = jersey_number
        p.position      = position
        p.team          = team
        p.save()

        return redirect('view_players')

    return render(request, 'players/add_player.html')


# Task 5 - View all players
def view_players(request):
    if not request.user.is_authenticated:
        return redirect('login')

    all_players = Player.objects.filter(user=request.user)
    return render(request, 'players/view_players.html', {'players': all_players})


# Task 6 - Edit a player
def edit_player(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    player = Player.objects.get(id=pk, user=request.user)

    if request.method == 'POST':
        player.name          = request.POST.get('name')
        player.jersey_number = request.POST.get('jersey_number')
        player.position      = request.POST.get('position')
        player.team          = request.POST.get('team')
        player.save()
        return redirect('view_players')

    return render(request, 'players/edit_player.html', {'player': player})


# Task 7 - Delete a player
def delete_player(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    player = Player.objects.get(id=pk, user=request.user)
    player.delete()
    return redirect('view_players')


# Task 8 - Signup
def signup_view(request):
    error = ''
    if request.method == 'POST':
        username  = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect('view_players')
        else:
            error = 'Passwords do not match.'

    return render(request, 'players/signup.html', {'error': error})


# Task 8 - Login
def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('view_players')
        else:
            error = 'Invalid username or password.'

    return render(request, 'players/login.html', {'error': error})


# Task 9 - Logout
def logout_view(request):
    logout(request)
    return redirect('login')
