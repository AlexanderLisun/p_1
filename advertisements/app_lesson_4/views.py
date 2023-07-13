from django.shortcuts import render
from django.http import HttpResponse

def index1(request):
    return HttpResponse('Домашка по 4 занятию')
# Create your views here.
