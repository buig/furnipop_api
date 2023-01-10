from rest_framework import serializers

from furnipop_api.models import Pedido

class PedidoSerializer(serializers.Serializer):
    fecha = serializers.CharField(max_length=45)
    camion_id = serializers.IntegerField()
    cliente_id = serializers.IntegerField()
    direccion_id = serializers.IntegerField()
    estado_pedido_id = serializers.IntegerField()
    metodo_pago_id = serializers.IntegerField()

    def create(self, validated_data):

        return Pedido.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.fecha = validated_data.get('fecha',instance.fecha)
        instance.camion_id = validated_data.get('camion_id',instance.camion_id)
        instance.cliente_id = validated_data.get('cliente_id',instance.cliente_id)
        instance.direccion_id = validated_data.get('direccion_id',instance.direccion_id)
        instance.estado_pedido_id = validated_data.get('estado_pedido_id',instance.estado_pedido_id)
        instance.metodo_pago_id = validated_data.get('metodo_pago_id',instance.metodo_pago_id)

        instance.save()

        return instance