from django.urls import path, include

from myteam import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.schedule, name='schedule'),
    path('', views.player, name='player'),
    path('', views.team, name='team'),

]
