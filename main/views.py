from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def blogHome(request):
    return HttpResponse('This is for home page of blog untill template added')
