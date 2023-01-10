from rest_framework import serializers

from furnipop_api.models import EstadoPedido

class EstadoPedidoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=10)

    def create(self, validated_data):

        return EstadoPedido.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.save()

        return instance