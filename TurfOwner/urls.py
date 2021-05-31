from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('homepage/',views.homepage,name="TurfOwnerHomePage"),
    path('addturfmanager/',views.AddTurfManager,name="AddTurfManager"),
    path('profile/',views.OwnerProfile,name="TurfOwnerProfile"),
    path('ownerLogout/',views.ownerLogout,name="TurfOwnerLogout")
]

