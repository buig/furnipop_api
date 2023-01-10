from rest_framework import serializers

from furnipop_api.models import Cliente

class ClienteSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=45)
    apellidos = serializers.CharField(max_length=45)
    dni = serializers.CharField(max_length=10)
    fecha_nacimiento = serializers.DateField()
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):

        return Cliente.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.apellidos = validated_data.get('apellidos',instance.apellidos)
        instance.dni = validated_data.get('dni',instance.dni)
        instance.fecha_nacimiento = validated_data.get('fecha_nacimiento',instance.fecha_nacimiento)
        instance.email = validated_data.get('email',instance.email)
        instance.password = validated_data.get('password',instance.password)

        instance.save()

        return instance