from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Stock
from .models import UserStock

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

def signup(request):
    """
        Purpose: The purpose of this particular function is to allow the user to
        create an account if they do not have one. It takes the username, password,
        first name, and last name of the user and saves the data. In the future, the
        user will be able to create a personalized stock list for their account.
    """
    if request.POST:
        newUser = User(
            username = request.POST['enterUname'],
            password = make_password(request.POST['enterPwd']),
            first_name = request.POST['enterFname'],
            last_name = request.POST['enterLname'],
        )
        newUser.save()
        template = loader.get_template('stocks/signup.html')
        context = {
            'user': newUser,
        }
        return HttpResponse(template.render(context, request))
    else:
        context = {
        }
        template = loader.get_template('stocks/signup.html')
        return HttpResponse(template.render(context, request))

def index(request):
    """
        Purpose: The purpose of this function is to authenticate the user's login.
        If their username and password are valid, then the user will be able to
        access their stock list/data. However, if the their username is invalid,
        then they won't be able to see or add to their stock list and when they go
        to the stocks page, they will only be able to see a generic stock page.
    """
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
# Trying to work on having the user input different stock data which will
# get transfered and displayed on their personalized stock list in the
# templates.
def stock(request):
    if request.POST:
        try:
            newStock = Stock.objects.get(sTicker=request.POST['Ticker'])

        except:
            newStock = Stock(
                fullName = request.POST['Company'],
                sTicker = request.POST['Ticker'],
                pEratio = request.POST['PE'],
                EPS = request.POST['newEPS'],
                Yield = request.POST['newYield'],
                Volume = request.POST['newVolume'],
                marketCap = request.POST['newCap'],
            )
            newStock.save()

        userStock = UserStock(
            stock = newStock,
            numShares = request.POST['newShares'],
            userName = request.user,
        )
        userStock.save()

    if request.user.is_authenticated:
        # Checks if the user has an account, otherwise redirects them to a
        # default page.
        template = loader.get_template('stocks/stock.html')
        uStocks = UserStock.objects.filter(userName=request.user)
        userStocks = []
        for ustock in uStocks:
            stockDict = {}
            stockDict["ustock"] = ustock
            userStock = Stock.objects.get(id=ustock.stock_id)
            stockDict["stockInfo"] = userStock
            userStocks.append(stockDict)

        context = {
            'uStocks': userStocks,
            'userInfo': request.user,
        }
        print(context)
        return HttpResponse(template.render(context, request))

    else:
        # if the user does not have a valid log in, then the nologinstock.html
        # will load for the user.
        template = loader.get_template('stocks/nologinstock.html')
        context = {
            # Nothing.
        }
        return HttpResponse(template.render(context, request))
