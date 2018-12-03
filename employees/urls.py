from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Employees, name="employees"),
    re_path(r'^add/$', views.add, name="add"),
    re_path(r'^addsuccess/$', views.addsuccess, name="addsuccess"),
    path('update/', views.UpdateEmployee, name="update"),
]