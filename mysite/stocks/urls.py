from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('stocks/', views.stock, name='stock'),
    path('funds/', views.fund, name='fund')
]
