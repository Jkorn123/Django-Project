from django.db import models

class Stocks(models.Model):
    #User can search up stocks.
    print("Get stocks the user wants.")

class Indexes(models.Model):
    #User can search up indexes.
    print("Get indexes the user wants.")

class ETFs(models.Model):
    #User can search up ETFs.
    print("Get the ETFs the user wants.")

class MutualFunds(models.Model):
    #User can search up mutual funds.
    print("Get the mutual funds the user wants.")
