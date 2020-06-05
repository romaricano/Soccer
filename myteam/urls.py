from django.urls import path, include

from myteam import views

urlpatterns = [
    path('', views.index, name='home'),

]
