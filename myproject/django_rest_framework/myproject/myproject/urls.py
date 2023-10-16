"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/','median.html', name='index'),
]
from django.urls import path
from . import views



urlpatterns = [
    path('total-records/', views.total_records, name='total_records'),
]

urlpatterns = [
    path('calculate-mean/', views.calculate_mean, name='calculate_mean'),
    path('calculate-median/', views.calculate_median, name='calculate_median'),
    path('calculate-percentile-25/', views.calculate_percentile_25, name='calculate_percentile_25'),
    path('calculate-percentile-75/', views.calculate_percentile_75, name='calculate_percentile_75'),
]
