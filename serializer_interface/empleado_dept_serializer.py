from rest_framework import serializers

from furnipop_api.models import Empleado

class EmpleadoDeptSerializer(serializers.ModelSerializer):
    dni = serializers.CharField(max_length=12)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
    nss = serializers.CharField(max_length=45)
    nombre = serializers.CharField(max_length=100)
    apellidos = serializers.CharField(max_length=100)


    class Meta:
        model = Empleado
        fields = ['dni', 'email',\
            'password', 'nss', 'nombre',\
            'apellidos']