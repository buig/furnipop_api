from rest_framework import serializers

from furnipop_api.models import Item

from .empleado_dept_serializer import EmpleadoDeptSerializer

class ItemSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        item = Item.objects.create(**validated_data)

        return item


    class Meta:
        model = Item
        fields = '__all__'