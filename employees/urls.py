from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Employees, name="employees"),
    re_path(r'^add/$', views.add, name="add"),
    re_path(r'^addsuccess/$', views.addsuccess, name="addsuccess"),
    path('deletesuccess/', views.deletesuccess, name="deletesuccess"),
    path('update/', views.UpdateEmployee, name="update"),
    re_path(r'^updatesuccess/$', views.updatesuccess, name="updatesuccess"),
]