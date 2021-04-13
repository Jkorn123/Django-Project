from django.contrib import admin
from .models import stockName, fundName, getdatePrice

admin.site.register(stockName)
admin.site.register(fundName)
admin.site.register(getdatePrice)
