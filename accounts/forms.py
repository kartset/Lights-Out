from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(AuthenticationForm):
  username=forms.CharField(widget=forms.TextInput(
  attrs={'class':'form-control', 'placeholder': 'Enter Username'}
  ), label="Username")
  password=forms.CharField(widget=forms.PasswordInput(
  attrs={'class':'form-control', 'placeholder': 'Enter Password'}
  ), label="Password")

class RegistrationForm(UserCreationForm):
  email=forms.EmailField(required=True)

  class Meta:
    model=User
    fields=(
      'username',
      'first_name',
      'last_name',
      'email',
      'password1',
      'password2'
    )

  def save(self, commit=True):
    user=super(RegistrationForm, self).save(commit=False)
    user.first_name=cleaned_data['first_name']
    user.last_name=cleaned_data['last_name']
    user.email=cleaned_data['email']

    if commit:
      user.save()
    return user




