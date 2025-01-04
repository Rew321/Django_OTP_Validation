
from django.contrib import admin
from django.urls import path
from OTP import views

urlpatterns = [
    path("", views.login, name = "login"),
    path('register', views.register, name="register"),
    path('cart', views.cart, name="cart"),
    path('otp', views.otp, name="otp"),
]
