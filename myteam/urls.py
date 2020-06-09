from django.urls import path, include

from myteam import views

urlpatterns = [
    path('', views.index, name='home'),
    path('schedule', views.schedule, name='schedule'),
    path('player', views.player, name='player'),
    path('team', views.team, name='team'),
]
