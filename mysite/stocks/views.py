from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Stock
from .models import Fund
from .models import Price

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
    sName = Stock.objects.all()
    context = {
        'sName': sName,
    }
    print(context)
    return HttpResponse(template.render(context, request))

def fund(request):
    template = loader.get_template('stocks/fund.html')
    fName = Fund.objects.all()
    context = {
        'fName': fName,
    }
    return HttpResponse(template.render(context, request))
