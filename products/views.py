from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Category
from django.contrib import messages
# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'products/dashboard.html')

def Products(request):
    return render(request, 'products/products.html')

def AddProduct(request):
    return HttpResponse("Add Product Page")

def UpdateProduct(request):
    return HttpResponse("Update Page Of Product")

def Categorys(request):
    catDetails = Category.objects.filter(user=request.user).all()
    return render(request,'products/category.html',{'Category' : catDetails })

@login_required
def AddCategory(request):
    return render(request, 'products/addcategory.html')

@login_required
def addcatsuccess(request):
    name = request.POST['name']
    description = request.POST['description']
    user = request.user
    addcat = Category(name=name,description=description,user=user)
    addcat.save()
    return redirect('products:category')

def UpdateCategory(request):
    return HttpResponse("Update Page Of Product")