from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from furnipop_api.models import Material

object_original = {'nombre':'Wood'}
object_update = {'nombre':'Stainless Steel'}
object_ref="Wood"
object_update_ref = "Stainless Steel"
multiple_route = "/materiales"
single_route = "/material/{pk}"


class MaterialTestCase(TestCase):

    def setUp(self):
        
        self.factory = APIClient()
        self.pk = None
        request = self.factory.post(multiple_route,object_original,format ='json')

    def is_object_created(self):
        color = Material.objects.get(nombre=object_ref)
        self.assertIsNotNone(color)

    def can_get_object(self):
        color = Material.objects.get(nombre=object_ref)
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