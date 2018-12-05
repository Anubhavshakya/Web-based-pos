from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'products/dashboard.html')

def Products(request):
    proDetails = Product.objects.all()
    return render(request,'products/products.html',{'Product' : proDetails })

def AddProduct(request):
   showCat = Category.objects.filter(user=request.user).all()
   return render(request,'products/addproduct.html',{'catDetails' : showCat })

@login_required
def addprodsuccess(request):
   category_id = request.POST.get('catData')
   unit_price = request.POST.get('unit_price')
   barcode = request.POST.get('barcode')
   reorder_level = request.POST.get('reorder_level')
   description = request.POST.get('description')
   user = request.user
   addprod = Product(description=description,barcode=barcode,unit_price=unit_price,reorder_level=reorder_level,category_id=category_id,user=user)
   addprod.save()
   return redirect('products:products')

@login_required
def deleteprodsuccess(request):
   prodid = request.POST.get("proddelete")
   userid = request.user
   query1 = Q(product_id = prodid)
   query2 = Q(user = userid)
   Product.objects.filter(query1 & query2).delete()
   return redirect('products:products')
   

def UpdateProduct(request):
   return HttpResponse("Update Page Of Product")

@login_required
def Categorys(request):
    catDetails = Category.objects.filter(user=request.user).all()
    return render(request,'products/category.html',{'Category' : catDetails })

@login_required
def deletecatsuccess(request):
   catid = request.POST.get("catdelete")
   userid = request.user
   query1 = Q(category_id = catid)
   query2 = Q(user = userid)
   Category.objects.filter(query1 & query2).delete()
   return redirect('products:categorys')



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
    return redirect('products:categorys')

"""@login_required
def showcat(request):
   showCat = Category.objects.filter(user=request.user).all()
   return render(request,'products/addproduct.html',{'catDetails' : showCat }) """

def UpdateCategory(request):
    return HttpResponse("Update Page Of Product")