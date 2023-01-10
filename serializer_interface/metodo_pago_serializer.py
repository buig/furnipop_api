from rest_framework import serializers

from furnipop_api.models import MetodoPago

class MetodoPagoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=45)
    cliente_id = serializers.IntegerField()

    def create(self, validated_data):

        return MetodoPago.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.cliente_id = validated_data.get('cliente_id',instance.cliente_id)

        instance.save()

        return instance