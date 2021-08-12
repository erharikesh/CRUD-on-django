
from django import forms
from  .models import User


class StudentRegistration(forms.Form):
 name = forms.CharField()
 email= forms.EmailField()
 password = forms.PasswordInput()