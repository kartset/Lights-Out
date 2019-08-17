from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from accounts.forms import LoginForm

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(authentication_form=LoginForm,template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='templates/home.html'), name="logout"),
]
