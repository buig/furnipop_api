from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from furnipop_api.models import Cliente

object_original = {"nombre": "Erhart",
        "apellidos": "Guilliatt",
        "dni": "60799988G",
        "fecha_nacimiento": "1987-06-28",
        "email": "eguilliatt0@hostgator.com",
        "password": "tPM1GZw"}
object_update = {"nombre": "Pedro",
        "apellidos": "Guilliatt",
        "dni": "60799988G",
        "fecha_nacimiento": "1987-06-28",
        "email": "eguilliatt0@hostgator.com",
        "password": "tPM1GZw"}
object_ref="Erhart"
object_update_ref = "Pedro"
multiple_route = "/clientes"
single_route = "/cliente/{pk}"


class ClienteTestCase(TestCase):

    def setUp(self):
        
        self.factory = APIClient()
        self.pk = None
        request = self.factory.post(multiple_route,object_original,format ='json')

    def is_object_created(self):
        color = Cliente.objects.get(nombre=object_ref)
        self.assertIsNotNone(color)

    def can_get_object(self):
        color = Cliente.objects.get(nombre=object_ref)
        self.pk = color.pk
        request_objects = self.factory.get(multiple_route)
        request_object = self.factory.get(single_route.format(pk = self.pk))
        self.assertContains(request_objects, object_ref)
        self.assertContains(request_object, object_ref)

    def can_update(self):
        request_object = self.factory.put(
            single_route.format(pk = self.pk), 
            object_update,format ='json')
        self.assertContains(request_object, object_update_ref)

    def can_delete(self):
        request_object = self.factory.delete(single_route.format(pk = self.pk))
        self.assertEquals(request_object.status_code, status.HTTP_204_NO_CONTENT)

    def test_material(self):
        self.is_object_created()
        self.can_get_object()
        self.can_update()
        self.can_delete()