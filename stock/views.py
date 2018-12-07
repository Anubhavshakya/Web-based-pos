from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
@login_required
def Stock(request):
    return render(request, 'stock.html')

@login_required
def addStock(request):
    return render(request, 'add.html')
