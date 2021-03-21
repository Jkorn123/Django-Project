from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
    # Template does not exist error???
    template = loader.get_template('stocks/index.html')
    return HttpResponse(template.render(request))

def stock(request):
    return HttpResponse("This is the stocks page.")

def fund(request):
    return HttpResponse("This is the funds page.")
