from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class UserForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ("username", "email", "password")

"""class UserProfileForm(forms.ModelForm):
        class Meta:
                model = Userprofile
                fields = ("address", "mobile")
"""

"""class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('availability', 'bio','teacher_logo')"""