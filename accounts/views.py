from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect 
from accounts.forms import UserForm,SignUpForm
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
"""def Signup(request):
    return render(request, "accounts/signup.html")"""

def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            messages.success(request,'Welcome To Web Based Point Of Sale')
            return redirect('products:dashboard')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

"""def Dashboard(request):
    return HttpResponse("Dashboard Works Fine")
"""
"""@login_required
@transaction.atomic
def Profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            saveuser = profile_form.save(commit=False)
            saveuser.user_id = request.user
            saveuser.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })"""
'''def afters(request):
    user_name = request.POST["user_name"]
    email_id = request.POST["email_id"]
    name = request.POST["name"]
    address = request.POST["address"]
    mobile = request.POST["mobile"]
    password = request.POST["password"]
    user = User(user_name = user_name, email_id = email_id, name = name, address = address, mobile = mobile, password = password)
    user.save()
    return render(request, "accounts/signup.html")'''

"""def Login(request):
   return render(request, "accounts/login.html")

def userlogin(request):
    
    if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  # Redirect to index page.
                  #return HttpResponseRedirect("accounts/signup.html")
                  return render(request,'home.html', {})
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print("invalid login details " + username + " " + password)
              return render(request,'accounts/login.html', {})
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request,'accounts/login.html', {})"""