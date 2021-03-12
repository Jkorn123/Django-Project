from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class homePage(generic.DetailView):
    print("sign up, log in")

class signupView(generic.DetailView):
    print("uname, pword, sign up")

class loginView(generic.DetailView):
    print("uname, pword, log in")

class stockView(generic.DetailView):
    print("stocks")

class indexView(generic.DetailView):
    print("indexes")

class ETFView(generic.DetailView):
    print("ETFs")

class mutualfundView(generic.DetailView):
    print("mutual funds")
