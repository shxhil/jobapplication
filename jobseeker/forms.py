from django import forms
from myapp.models import StudentProfile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2","first_name"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        exclude=("user","saved_jobs")