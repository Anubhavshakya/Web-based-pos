from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Stock, name="stock"),
    path('add/', views.addStock, name="addStock"),

]