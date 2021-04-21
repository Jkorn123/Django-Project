from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Stock
from .models import Fund
from .models import Price

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    # Will work on the user authentication after the templates and models are
    # complete. (Not done yet)
#    if request.POST:
#        if 'enterUname' in request.POST.keys():
#            user = authenticate(username=request.POST['enterUname'],
#                password=request.POST['enterPwd'])
#            if user is not None:
#                login(request, user)
#            else:
#                pass
#         elif 'logout' in request.POST.keys():
#            logout(request)
#    if request.user.is_authenticated:
#        loggedIn = True
#    else:
#        loggedIn = False

    template = loader.get_template('stocks/index.html')
    context = {
    # Blank for now.
    }
    return HttpResponse(template.render(context, request))

# Working on getting the forms to be linked to this particular view.
def stock(request):
    template = loader.get_template('stocks/stock.html')
    sName = Stock.objects.all()
    context = {
        'sName': sName,
    }
    return HttpResponse(template.render(context, request))

def fund(request):
    template = loader.get_template('stocks/fund.html')
    fName = Fund.objects.all()
    context = {
        'fName': fName,
    }
    return HttpResponse(template.render(context, request))
