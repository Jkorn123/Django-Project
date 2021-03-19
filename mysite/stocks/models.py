from django.db import models
from django.contrib.auth.models import User

class Stocks(models.Model):
    stockName = models.CharField(max_length=30)
    def __str__(self):
        return self.stockName

class Funds(models.Model):
    fundName = models.CharField(max_length=30)
    def __str__(self):
        return self.fundName
