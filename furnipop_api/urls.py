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
from django.conf.urls.static import static
from django.conf import settings
#from settings import MEDIA_URL,MEDIA_ROOT
from . import views

from controller import colors
from controller import departamentos
from controller import contenedores
from controller import imagenes
from controller import materiales
from controller import estados_items
from controller import empleados
from controller import lotes
from controller import items
from controller import pedidos
from controller import clientes
from controller import direcciones
from controller import metodos_pago
from controller import paypal
from controller import tarjetas
from controller import camiones
from controller import estados_pedido


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
    path('materiales',materiales.getOrPostMaterial,name='materiales'),
    path('material',materiales.getPutDeleteMaterial,name='material'),
    path('estados-items',estados_items.getOrPostEstadoItem,name='materiales'),
    path('estado-item',estados_items.getPutDeleteEstadoItem,name='material'),
    path('empleados',empleados.getOrPostEmpleado,name='empleados'),
    path('empleado',empleados.getPutDeleteEmpleado,name='empleado'),
    path('departamento/empleados',empleados.getEmpleadosFromDepartamento,name="departamento empleados"),
    path('departamento/empleado',empleados.putEmpleadoInDepartamento,name="departamento empleado"),
    path('lotes',lotes.getOrPostLote,name='lotes'),
    path('lote',lotes.getPutDeleteLote,name='lote'),
    path('lote/items',items.getItemsByLote,name='items in lote'),
    path('lote/item',items.getPutDeleteItemFromLote,name='item in lote'),
    path('items',items.getOrPostItem,name='items'),
    path('item',items.getPutDeleteItem,name='item'),
    path('pedidos',pedidos.getOrPostPedido,name='pedidos'),
    path('pedido',pedidos.getPutDeletePedido,name='pedido' ),
    path('pedido/items',items.getItemsByPedido,name='items in pedido'),
    path('pedido/item',items.getPutDeleteItemFromPedido,name='item in pedido' ),
    path('pedido/lotes',lotes.getLotesByPedido,name='lotes in pedido'),
    path('pedido/lote',lotes.getPutDeleteLoteFromPedido,name='lote in pedido' ),
    path('clientes',clientes.getOrPostCliente,name='clientes'),
    path('cliente',clientes.getPutDeleteCliente,name='cliente'),
    path('direcciones',direcciones.getOrPostdireccion,name='direcciones'),
    path('direccion',direcciones.getPutDeleteDireccion,name='direccion'),
    path('metodos-pago',metodos_pago.getOrPostMetodosPago,name='metodo-pago'),
    path('metodo-pago',metodos_pago.getPutDeleteMetodoPago,name='metodo-pago'),
    path('paypals',paypal.getPaypal,name='paypals'),
    path('paypal',paypal.getPutDeletePaypal,name='paypal'),
    path('tarjetas',tarjetas.getTarjeta,name='tarjetas'),
    path('tarjeta',tarjetas.getPutDeleteTarjeta,name='tarjeta'),
    path('camiones',camiones.getOrPostCamion,name='camiones'),
    path('camion',camiones.getPutDeleteCamion,name='camion'),
    path('estados-pedido',estados_pedido.getOrPostEstadoPedido,name='estados-pedido'),
    path('estado-pedido',estados_pedido.getPutDeleteEstadoPedido,name='estado-pedido'),
    path('login-empleado',empleados.validateEmpleado,name='login-empleado'),
    path('login-cliente',clientes.validateCliente,name='login-cliente')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
