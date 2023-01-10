from rest_framework import serializers

from furnipop_api.models import Direccion

class DireccionSerializer(serializers.Serializer):
    linea1 = serializers.CharField(max_length=200)
    linea2 = serializers.CharField(max_length=45)
    codigo_postal = serializers.CharField(max_length=45)
    ciudad = serializers.CharField(max_length=45)
    provincia = serializers.CharField(max_length=45)
    cliente_id = serializers.IntegerField()

    def create(self, validated_data):

        return Direccion.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.linea1 = validated_data.get('linea1',instance.linea1)
        instance.linea2 = validated_data.get('linea2',instance.linea2)
        instance.codigo_postal = validated_data.get('codigo_postal',instance.codigo_postal)
        instance.ciudad = validated_data.get('ciudad',instance.fecha_nacimiento)
        instance.provincia = validated_data.get('provincia',instance.provincia)
        instance.cliente_id = validated_data.get('cliente_id',instance.cliente_id)

        instance.save()

        return instance