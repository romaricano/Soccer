from django.shortcuts import render




# Create your views here.

def index(request):
    return render(request, 'pages/player-list-gallery.html')

def schedule(request):
    return render(request, 'pages/schedule-widget-style.html')

def player(request):
    return render(request, 'pages/player-list-gallery.html')


def team(request):
    return render(request, 'pages/about-our-team.html')

# Create your views here.
