"""
URL configuration for django_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from .views import main_view
from .views import predict_api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('nlp_app/', include('nlp_app.urls')),
    path('', main_view, name='main'),  # Esto hace que la URL vacía ('') de django_app redirija a main_view
    path('predict_api/', predict_api, name='predict_api'),  # Endpoint para AJAX

]
