from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

class homePage(generic.DetailView):
    return "sign up, log in"

class signupView(generic.DetailView):
    return "uname, pword, sign up"

class loginView(generic.DetailView):
    return "uname, pword, log in"

class stockView(generic.DetailView):
    # This will be where the user will be able to view different stocks of
    # their choosing.
