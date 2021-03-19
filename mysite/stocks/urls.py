from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('stock/', views.stock, name='stock'),
    path('index/', views.index, name='index'),
    path('ETF/', views.etf, name='etf'),
    path('mutualfund/', views.mutualfund, name='mutualfund'),
]
