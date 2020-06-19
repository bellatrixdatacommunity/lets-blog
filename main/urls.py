from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome, name='bolg-home')  #for home page of blog

]