from django.urls import path
from . import views

userLoggedIn = False
if userLoggedIn == True:
    urlpatterns = [
        path('', views.homePage.as_view(), name='home'),
        path('home/', views.signupView.as_view(), name='signup'),
        path('home/', views.loginView.as_view(), name='login'),
        path('home/stocks/', views.stockView, name='stocks'),
        path('home/indexes/', views.indexView, name='indexes'),
        path('home/ETFs/', views.ETFView, name='ETFs'),
        path('home/mutualfunds/', views.mutalfundView, name='Mutual Funds')

    ]
# If the user does not have a log in, they will be unable to access certain pages
# within the webpage. A user without a login and a password will only be unable
# to access stocks, indexes, ETFs, and mutual funds.
else:
    urlpatterns = [
        path('', views.homePage.as_view(), name='home'),
        path('home/', views.signupView.as_view(), name='signup'),
        path('home/', views.loginView.as_view(), name='login'),

    ]
