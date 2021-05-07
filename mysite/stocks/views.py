from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Stock
from .models import Fund
from .models import Price

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

def signup(request):
    template = loader.get_template('stocks/signup.html')
    context = {}
    return HttpResponse(template.render(context, request))
#    newUser = User(
#        username = request.POST['username']
#        password = make_password(request.POST['password'])
#
#    )
#    newUser.save()


def index(request):
    # Will work on the user authentication after the templates and models are
    # complete. (Not done yet)
    if request.POST:
        if 'enterUname' in request.POST.keys():
            user = authenticate(username=request.POST['enterUname'],
                password=request.POST['enterPwd'])
            if user is not None:
                login(request, user)
                print('loggedIn')
            else:
                print('loggedIn failed')
        elif 'logout' in request.POST.keys():
            logout(request)
    if request.user.is_authenticated:
        loggedIn = True
    else:
        loggedIn = False

    template = loader.get_template('stocks/index.html')
    context = {
        'loggedIn': loggedIn,
        'user': request.user,
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
