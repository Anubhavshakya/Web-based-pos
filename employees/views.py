from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Employee
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
@login_required
def Employees(request):
    empDetails = Employee.objects.filter(user=request.user).all()
    return render(request,'employees/employees.html',{'Employee' : empDetails })
@login_required
def add(request):
    return render(request,'employees/add.html')

@login_required
def addsuccess(request):
    name = request.POST.get('name')
    salary = request.POST.get('salary')
    role = request.POST.get('role')
    mobile = request.POST.get('mobile')
    address = request.POST.get('address')
    user = request.user
    employee = Employee(user=user, name=name, salary=salary, role=role, contact=mobile,address=address)
    employee.save()
    return redirect('employees:employees')
    #return render(request,'employees/employees.html',{})

@login_required
def updatesuccess(request):
    id = request.POST.get('emp_id')
    salary = request.POST.get('salary')
    role = request.POST.get('role')
    Employee.objects.filter(emp_id=id).update(salary=salary, role=role)
    return redirect('employees:employees')

@login_required
def UpdateEmployee(request):
    return render(request,'employees/update.html')