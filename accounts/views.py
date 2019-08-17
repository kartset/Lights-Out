from django.shortcuts import render
from accounts.forms import RegistrationForm
from accounts.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect


class SignUp(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def register(request):
  if request.method =='POST':
    form=RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return(redirect('/accounts'))
  else:
    form=RegistrationForm()
    args={'form': form}
    return render(request, 'templates/signup.html', args)
