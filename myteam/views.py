from django.shortcuts import render




# Create your views here.

def index(request):
    return render(request, 'pages/home.html')

def schedule(request):
    return render(request, 'pages/schedule-widget-style.html')

def player(request):
    return render(request, 'pages/player-list-gallery.html')

def team(request):
    return render(request, 'pages/liverpool.html')

def league(request):
    return render(request, 'pages/league-table.html')

def contact(request):
    return render(request, 'pages/contact.html')
# Create your views here.
