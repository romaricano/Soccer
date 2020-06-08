from django.shortcuts import render
import datetime
from . import models


# Create your views here.

def index(request):
    data = {'players': models.Player.objects.filter(status=True),
            'matchs': models.Match.objects.all(),
            'matchs2':models.Match.objects.filter(date__gte=datetime.date.today()).filter(equipeA__nom='Barcelone')}
    return render(request, 'pages/home.html', data)


def schedule(request):
    matchs = {'matchs': models.Match.objects.all()}
    return render(request, 'pages/schedule-widget-style.html', matchs)


def player(request):
    data = {'players': models.Player.objects.filter(status=True, team__nom='Barcelone'),
            'postes': models.Poste.objects.filter(status=True)}

    return render(request, 'pages/player-list-gallery.html', data)


def team(request):
    data = {'players': models.Player.objects.filter(status=True,),
            'matchs': models.Match.objects.filter(equipeA__nom='Barcelone'),
            'team': models.Team.objects.filter(nom__exact='Barcelone'),
            'postes': models.Poste.objects.filter(status=True)}
    return render(request, 'pages/liverpool.html', data)


def league(request):
    return render(request, 'pages/league-table.html')


def contact(request):
    return render(request, 'pages/contact.html')
# Create your views here.
