from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from furnipop_api.models import Contenedor

object_original = {"referencia":"HMYM",'fecha_alta':'2021-12-22T00:00:00Z'}
object_update = {"referencia":"HMYM",'fecha_alta':'2023-12-22T00:00:00Z'}

class ContenedorTestCase(TestCase):

    def setUp(self):
        
        self.factory = APIClient()
        self.pk = None
        request = self.factory.post('/contenedores',object_original,format ='json')

    def is_object_created(self):
        object = Contenedor.objects.get(referencia="HMYM")
        self.assertIsNotNone(object)

    def can_get_object(self):
        object = Contenedor.objects.get(referencia="HMYM")
        self.pk = object.pk
        request_colores = self.factory.get('/contenedores')
        request_color = self.factory.get('/contenedor/{pk}'.format(pk = self.pk))
        self.assertContains(request_colores, "HMYM")
        self.assertContains(request_color, "HMYM")

    def can_update(self):
        request_object = self.factory.put(
            '/contenedor/{pk}'.format(pk = self.pk), 
            object_update,format ='json')
        self.assertContains(request_object, "2023-12-22T00:00:00Z")

    def can_delete(self):
        request_object = self.factory.delete('/contenedor/{pk}'.format(pk = self.pk))
        self.assertEquals(request_object.status_code, status.HTTP_204_NO_CONTENT)

    def test_contenedores(self):
        self.is_object_created()
        self.can_get_object()
        self.can_update()
        self.can_delete()