from django.urls import path
from . import views
from django.conf import settings
#from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
#from django.views.generic.base import TemplateView

urlpatterns = [

    path('accounts/login/issues/', views.issue_list, name='issue_list'),
    path('accounts/login/issues/water/', views.issue_water, name='issue_water'),
    path('accounts/login/issues/air/', views.issue_air, name='issue_air'),
    path('accounts/login/issues/land/', views.issue_land, name='issue_land'),
    path('accounts/login/issues/forest/', views.issue_forest, name='issue_forest'),
    path('accounts/login/issues/energy/', views.issue_energy, name='issue_energy'),
    path('accounts/login/issues/waste/', views.issue_waste, name='issue_waste'),
    path('accounts/login/issues/wildlife/', views.issue_wildlife, name='issue_wildlife'),


]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
