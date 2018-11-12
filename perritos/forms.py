from django import forms
from perritos.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
   class Meta():
    password = widget=forms.TextInput(attrs={'type' : 'password'})
    model = User
    fields = ('username','password','email')
    help_texts = {
            'username': None,
            'email': None,
        }

class UserProfileInfoForm(forms.ModelForm):
 
 class Meta():
  model = UserProfileInfo
  fields = ('rut','comuna','foto_perfil')