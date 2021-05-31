from django.db import models
from django.contrib.auth.models import User


class Stock(models.Model):
    # Different fields containing different kinds of data, will eventually
    # organize them into a table in which the user will be able to read.
    # Will create a graph of the stock displaying the change in price.
    fullName = models.CharField(max_length=120)
    sTicker = models.CharField(max_length=10)
    pEratio = models.FloatField(default=0.00)
    EPS = models.FloatField(default=0.00)
    Yield = models.FloatField(default=0.00)
    Volume = models.FloatField(default=0.00)
    marketCap = models.FloatField(default=0.00)

    def __str__(self):
        return self.fullName

class UserStock(models.Model):
    userName = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,

    )
    numShares = models.IntegerField(default=0)
