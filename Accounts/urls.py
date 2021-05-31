from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path("ownerRegistration/",views.OwnerRegistration,name=""),
    path("login/",views.login,name=""),
    
]

