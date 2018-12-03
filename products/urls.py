from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('products/', views.Products, name="products"),
    path('category', views.Categorys, name="categorys"),
    path('products/add/', views.AddProduct, name="AddProduct"),
    path('products/update/', views.UpdateProduct, name="UpdateProduct"),
    path('category/add/', views.AddCategory, name="addcategory"),
    path('category/addcatsuccess', views.addcatsuccess, name="addcatsuccess"),
    path('category/update/', views.UpdateCategory, name="UpdateCategory"),
]