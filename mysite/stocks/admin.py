from django.contrib import admin
from .models import Stock, Fund, Price

admin.site.register(Stock)
admin.site.register(Fund)
admin.site.register(Price)
