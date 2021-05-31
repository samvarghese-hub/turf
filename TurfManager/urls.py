from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('homepage/',views.homepage,name="TurfManagerHomePage"),
    # path('addturf/',views.AddTurfManager,name="AddTurfManager"),
    path('profile/',views.ManagerProfile,name="TurfManagerProfile"),
    path('ownerLogout/',views.ManagerLogout,name="TurfManagerLogout")
]