# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Contenedor(models.Model):
    referencia = models.CharField(max_length=45)
    fecha_alta = models.DateTimeField()
    ubicacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'contenedor'

class Color(models.Model):
    nombre = models.CharField(max_length=45)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'color'

class Material(models.Model):
    nombre = models.CharField(max_length=45)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'material'

class EstadoItem(models.Model):
    nombre = models.CharField(max_length=45)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'estado_item'


class Departamento(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'departamento'

class Empleado(models.Model):
    dni = models.CharField(unique=True, max_length=12)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    nss = models.CharField(unique=True, max_length=45)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'empleado'

class Item(models.Model):
    titulo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    alto = models.IntegerField()
    ancho = models.IntegerField()
    fecha_alta = models.DateField()
    preferencias = models.CharField(max_length=45, blank=True, null=True)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    contenedor = models.ForeignKey(Contenedor, models.DO_NOTHING)
    color = models.ForeignKey(Color, models.DO_NOTHING, blank=True, null=True)
    material = models.ForeignKey(Material, models.DO_NOTHING, blank=True, null=True)
    estado_item = models.ForeignKey(EstadoItem, models.DO_NOTHING, blank=True, null=True)
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'item'

class Cliente(models.Model):
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    dni = models.CharField(unique=True, max_length=10)
    fecha_nacimiento = models.DateField()
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'cliente'

class EstadoPedido(models.Model):
    nombre = models.CharField(max_length=45)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'estado_pedido'

class Direccion(models.Model):
    linea1 = models.CharField(max_length=200)
    linea2 = models.CharField(max_length=45, blank=True, null=True)
    codigo_postal = models.CharField(max_length=45)
    ciudad = models.CharField(max_length=45)
    provincia = models.CharField(max_length=45)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'direccion'

class Camion(models.Model):
    matricula = models.CharField(unique=True, max_length=10)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'camion'

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=45)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'metodo_pago'

class Pedido(models.Model):
    fecha = models.CharField(max_length=45)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    estado_pedido = models.ForeignKey(EstadoPedido, models.DO_NOTHING)
    direccion = models.ForeignKey(Direccion, models.DO_NOTHING, blank=True, null=True)
    camion = models.ForeignKey(Camion, models.DO_NOTHING, blank=True, null=True)
    metodo_pago = models.ForeignKey(MetodoPago, models.DO_NOTHING)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'pedido'

class Paypal(models.Model):
    email = models.CharField(unique=True, max_length=45)
    metodo_pago = models.ForeignKey(MetodoPago, models.DO_NOTHING)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'paypal'

class Tarjeta(models.Model):
    numero = models.CharField(unique=True, max_length=16)
    fecha_caducidad = models.CharField(max_length=45)
    cvv = models.CharField(max_length=45)
    metodo_pago = models.ForeignKey(MetodoPago, models.DO_NOTHING)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'tarjeta'

class Lote(models.Model):
    nombre = models.CharField(max_length=45)
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    items = models.ManyToManyField(Item, through='ItemsLotes')

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'lote'

class ItemsLotes(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField()

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'items_lotes'

class ItemsPedidos(models.Model):
    pedido = models.OneToOneField('Pedido', models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey(Item, models.DO_NOTHING)
    cantidad = models.IntegerField()

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'items_pedidos'
        unique_together = (('pedido', 'item'),)

class LotesPedidos(models.Model):
    lote = models.OneToOneField(Lote, models.DO_NOTHING, primary_key=True)
    pedido = models.ForeignKey('Pedido', models.DO_NOTHING)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'lotes_pedidos'
        unique_together = (('lote', 'pedido'),)

class Imagen(models.Model):
    src = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'imagen'

class ImagenesItems(models.Model):
    item = models.OneToOneField('Item', models.DO_NOTHING, primary_key=True)
    imagen = models.ForeignKey(Imagen, models.DO_NOTHING)

    class Meta:
        app_label = 'furnipop_api'
        db_table = 'imagenes_items'
        unique_together = (('item', 'imagen'),)

