from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import stockName, fundName, getdatePrice

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    template = loader.get_template('stocks/index.html')
    context = {
    # Blank for now.
    }
    return HttpResponse(template.render(context, request))

def stock(request):
    template = loader.get_template('stocks/stock.html')
    sName = stockName.objects.all()
    context = {
        'stockname': sName,
    }
    return HttpResponse(template.render(context, request))

def fund(request):
    template = loader.get_template('stocks/fund.html')
    fName = fundName.objects.all()
    context = {
        'fundname': fName,
    }
    return HttpResponse(template.render(context, request))
