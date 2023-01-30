from rest_framework import serializers
from rest_framework.response import Response

from furnipop_api.models import Item, Imagen

from .empleado_dept_serializer import EmpleadoDeptSerializer
from .imagen_serializer import ImagenSerializer

class ItemSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        item = Item.objects.create(**validated_data)

        return item


    class Meta:
        model = Item
        fields = '__all__'

class ItemImagenSerializer(serializers.ModelSerializer):

    imagenes = ImagenSerializer(many=True)

    class Meta:
        model = Item
        fields = '__all__'