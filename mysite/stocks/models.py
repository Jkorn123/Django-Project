from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    fullName = models.CharField(max_length=120)
    sTicker = models.CharField(max_length=10)
    pEratio = models.FloatField()
    EPS = models.FloatField()
    Yield = models.FloatField()
    Volume = models.FloatField()
    marketCap = models.FloatField()
    userName = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    def __str__(self):
        return self.fullName

class Fund(models.Model):
    fullName = models.CharField(max_length=120)
    fTicker = models.CharField(max_length=10)
    pEratio = models.FloatField()
    EPS = models.FloatField()
    Yield = models.FloatField()
    Volume = models.FloatField()
    netAssets = models.FloatField(
    )
    userName = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    def __str__(self):
        return self.fullName


class Price(models.Model):
    date = models.DateTimeField('Day price')
    price = models.FloatField(default=0.00)
#    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    def __str__(self):
        return self.date
