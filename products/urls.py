from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('products/', views.Products, name="products"),
    path('category', views.Categorys, name="categorys"),
    path('products/add/', views.AddProduct, name="addproduct"),
    path('products/addprodsuccess/', views.addprodsuccess, name="addprodsuccess"),
    path('products/deleteprodsuccess/', views.deleteprodsuccess, name="deleteprodsuccess"),  
    path('products/update/', views.UpdateProduct, name="updateproduct"),
    path('products/updateproductsuccess/', views.updateproductsuccess, name="updateproductsuccess"),
    path('category/add/', views.AddCategory, name="addcategory"),
    path('category/addcatsuccess/', views.addcatsuccess, name="addcatsuccess"),
    path('category/update/', views.UpdateCategory, name="UpdateCategory"),
    path('category/catupdatesuccess/', views.catupdatesuccess, name="catupdatesuccess"),
    path('category/deletecatsuccess/', views.deletecatsuccess, name="deletecatsuccess"),
]