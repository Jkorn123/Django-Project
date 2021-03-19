from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
    return HttpResponse("This is the home page.")

def stock(request):
    return HttpResponse("This is the stocks page.")

def fund(request):
    return HttpResponse("This is the funds page.")
