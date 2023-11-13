from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.home,name='home'),
    path("home",views.home,name='home'),
    path("router",views.router,name='router'),
    path("service",views.service,name='service'),
    path("contact",views.contact,name='contact'),
]