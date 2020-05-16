from django.urls import path

from . import views


urlpatterns=[
path('', views.index, name='index'),
path('home', views.index1search, name='index1search'),


]