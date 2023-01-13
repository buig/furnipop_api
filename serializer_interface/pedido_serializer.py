from rest_framework import serializers

from furnipop_api.models import Pedido

class PedidoSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        return Pedido.objects.create(**validated_data)

    class Meta:
        model = Pedido
        fields = '__all__'
