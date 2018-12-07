from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Employee
from django.http import HttpResponse
from django.db.models import Q
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
def deletesuccess(request):
    empid = request.POST.get('empdelete')
    userid = request.user
    query1 = Q(emp_id = empid)
    query2 = Q(user = userid)
    Employee.objects.filter(query1 & query2).delete()
    return redirect('employees:employees')

@login_required
def UpdateEmployee(request):
    return render(request,'employees/update.html')

"""def getEmpid(request):
    empid = request.POST['empupdate']
    return """

@login_required
def updatesuccess(request):
    if request.method == 'POST':
        dataid = request.POST.get('emp_id')
        salarydata = request.POST.get('salary')
        roledata = request.POST.get('role')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        empdata = Employee.objects.get(pk=dataid)
        empdata.salary = salarydata
        empdata.role = roledata
        empdata.mobile = mobile
        empdata.address = address
        empdata.save(force_update=True)
        return redirect('employees:employees')