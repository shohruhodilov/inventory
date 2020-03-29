"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
   path('', index, name='index'),
   path('laptop/', laptop_views, name='laptop_views'),
   path('desktop/', desktop_views, name='desktop_views'),
   path('mobile/', mobile_views, name='mobile_views'),
   path('add_laptop/', add_laptop, name='add_laptop'),
   path('add_desktop/', add_desktop, name='add_desktop'),
   path('add_mobile/', add_mobile, name='add_mobile'),
   path('edit_laptop/<int:pk>/', edit_laptop, name='edit_laptop'),
   path('edit_desktop/<int:pk>/', edit_desktop, name='edit_desktop'),
   path('edit_mobile/<int:pk>/', edit_mobile, name='edit_mobile'),
   path('delete_laptop/<int:pk>/', delete_laptop, name='delete_laptop'),
   path('delete_desktop/<int:pk>/', delete_desktop, name='delete_desktop'),
   path('delete_mobile/<int:pk>/', delete_mobile, name='delete_mobile')

]
