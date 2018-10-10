"""pm25project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from pm25.views import home,pm25s,delete,dw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('pm25',pm25s,name='cx_pm25'),
    path('delete',delete,name="delete"),
    path('dw',dw,name="dw"),
]
