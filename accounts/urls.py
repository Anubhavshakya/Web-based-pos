from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.Signup, name="Signup"),
    #path('', views.Dashboard, name="Dashboard"),
    #path('profile/', views.Profile, name="Profile"),
    #path('afters/', views.afters, name="afters"),
    #path('', include('django.contrib.auth.urls')),
    #path('accounts/login','django.contrib.auth.view.login'),
    #path('userlogin/', views.userlogin, name="userlogin" ),
]