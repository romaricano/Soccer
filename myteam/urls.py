from django.urls import path, include

from myteam import views
# from blog import views

urlpatterns = [
    path('', views.index, name='home'),
    path('schedule', views.schedule, name='schedule'),
    path('player', views.player, name='player'),
    path('team', views.team, name='team'),
    path('league', views.league, name='league'),
    path('contact', views.contact, name='contact'),
    # path('blog', views.blog, name='blog'),

]
