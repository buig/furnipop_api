from rest_framework import serializers

from furnipop_api.models import Lote, Empleado

from .empleado_dept_serializer import EmpleadoDeptSerializer

class LoteSerializer(serializers.ModelSerializer):

    empleado = EmpleadoDeptSerializer()

    def create(self, validated_data):
        empleado_data = validated_data.pop('empleado')
        one_entry = Empleado.objects.get(pk=empleado_data['id'])
        lote = Lote.objects.create(empleado = one_entry,**validated_data)

        return lote

    def update(self, instance, validated_data):

        instance.nombre = validated_data.get('nombre',instance.nombre)
        try:
            empleado_data = validated_data.pop('empleado')
            empleado = Empleado.objects.get(pk=empleado_data['id'])
            instance.empleado = empleado
        except Empleado.DoesNotExist:
            print('')
        finally:
            instance.save()

            return instance

    class Meta:
        model = Lote
        fields = ['id','nombre','empleado']