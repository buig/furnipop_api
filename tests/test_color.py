from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from furnipop_api.models import Color

color_crimson = {'nombre':'crimson'}
color_update = {'nombre':'yellow'}

class ColorTestCase(TestCase):

    def setUp(self):
        
        self.factory = APIClient()
        self.pk = None
        request = self.factory.post('/colores',color_crimson,format ='json')

    def is_object_created(self):
        color = Color.objects.get(nombre="crimson")
        self.assertIsNotNone(color)

    def can_get_object(self):
        color = Color.objects.get(nombre="crimson")
        self.pk = color.pk
        request_colores = self.factory.get('/colores')
        request_color = self.factory.get('/color/{pk}'.format(pk = self.pk))
        self.assertContains(request_colores, "crimson")
        self.assertContains(request_color, "crimson")

    def can_update(self):
        request_color = self.factory.put(
            '/color/{pk}'.format(pk = self.pk), 
            color_update,format ='json')
        self.assertContains(request_color, "yellow")

    def can_delete(self):
        request_color = self.factory.delete('/color/{pk}'.format(pk = self.pk))
        self.assertEquals(request_color.status_code, status.HTTP_204_NO_CONTENT)

    def test_colors(self):
        self.is_object_created()
        self.can_get_object()
        self.can_update()
        self.can_delete()