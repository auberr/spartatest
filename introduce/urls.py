from django.contrib import admin
from django.urls import path
from introduce import views

urlpatterns = [
    path('introduce/', views.introduce),
]
