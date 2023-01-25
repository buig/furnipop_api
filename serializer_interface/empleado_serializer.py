from rest_framework import serializers

from furnipop_api.models import Empleado, Departamento
from .departamento_serializer import DepartamentoSerializer

class EmpleadoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    dni = serializers.CharField(max_length=12)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
    nss = serializers.CharField(max_length=45)
    nombre = serializers.CharField(max_length=100)
    apellidos = serializers.CharField(max_length=100)

    def update(self, instance, validated_data):

        instance.password = validated_data.get('password',instance.password)
        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.apellidos = validated_data.get('apellidos',instance.apellidos)

        instance.save()

        return instance

    def updateDept(self,instance,departamento):
        instance.departamento = departamento

        instance.save()

        return instance
        
    class Meta:
        model = Empleado
        fields = ['id','dni', 'email',\
            'password', 'nss', 'nombre',\
            'apellidos', 'departamento']