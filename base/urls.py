from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [

    path('work',views.work,name="work"),
    path('contact',views.contact,name="contact"),
    path('services',views.services,name="services"),
    path('about',views.about,name="about"),
    path('history',views.history,name="history"),
    path('leaders',views.leaders,name="leaders"),
    path('values',views.values,name="values"),
    path('clients',views.clients,name="clients"),
    path('certifications',views.certifications,name="certifications"),
    path('faq',views.faq,name="faq"),
    path('',views.home,name="home"),
    path('index',views.home,name="home"),
    path('home',views.home,name="home")
    ,]