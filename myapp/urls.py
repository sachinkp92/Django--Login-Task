from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index,name='home'),
    path('login/', views.BasicDetails, name='login'),
]

