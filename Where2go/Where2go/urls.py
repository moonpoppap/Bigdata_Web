"""Where2go URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Trip import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('QuestionOpen',views.Question),
    path('Jim',views.Jim),
    path('Corn',views.Corn),
    path('Chokchai',views.Chokchai),
    path('Sufficiency',views.Sufficiency),
    path('Mountain',views.Mountain),
    path('Waterfall',views.Waterfall),
    path('Park',views.Park),
    path('Garden',views.Garden),
    path('Island',views.Island),
    path('ChaAm',views.ChaAm),
    path('HuaHin',views.HuaHin),
    path('Chaweng',views.Chaweng),
    path('Rattanakosin',views.Rattanakosin),
    path('Siam',views.Siam),
    path('Temple',views.Temple),
    path('Historic',views.Historic),
    path('GreenHill',views.GreenHill),
    path('LivePark',views.LivePark),
    path('DreamWorld',views.DreamWorld),
    path('SafariWorld',views.SafariWorld),
    path('Comment',views.CommentPredict),
    path('TripPredict',views.TripPredict),
    path('Home',views.Home)
]
