from django.db import models
from django.contrib.auth.models import User

class Stocks(models.Model):
    """
    Purpose: This function will search up the user's desired stock from some
    database and eventually display different statistics about that stock.
    """
    userStock = models.CharField(max_length=30)
    print("Get stocks the user wants.")

class Indexes(models.Model):
    index = models.CharField(max_length=30)
    print("Get indexes the user wants.")

class ETFs(models.Model):
    ETF = models.CharField(max_length=30)
    print("Get the ETFs the user wants.")

class MutualFunds(models.Model):
    mutualFund = models.CharField(max_length=30)
    print("Get the mutual funds the user wants.")
