"""furnipop_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from . import views

from controller import colors
from controller import departamentos
from controller import contenedores
from controller import imagenes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index, name='indice'),
    path('colores', colors.getOrPostColor, name='colores' ),
    path('color', colors.getPutDeleteColor, name='colores' ),
    path('departamentos',departamentos.getOrPostDepartamento,name='departamentos'),
    path('departamento',departamentos.getPutDeleteDepartamento,name='departamento'),
    path('contenedores',contenedores.getOrPostContenedor,name='contenedores'),
    path('contenedor',contenedores.getPutDeleteContenedor,name='contenedor'),
    path('imagenes',imagenes.getOrPostImagen,name='imagenes'),
    path('imagen',imagenes.getPutDeleteImagen,name='imagen'),
]
