from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('stocks/home.html')
    return HttpResponse(template.render(request))

def stock(request, stocks):
    return HttpResponse("This is the stocks page")

def index(request, indexes):
    return HttpResponse("This is the indexes page")

def etf(request, etfs):
    return HttpResponse("This is the ETF's page")

def mutualfund(request, mutualfunds):
    return HttpResponse("This is the mutual funds page")
