from rest_framework import serializers

from furnipop_api.models import Pedido
from .item_serializer import ItemImagenSerializer
from .lote_serializer import LoteSerializer

class PedidoSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        return Pedido.objects.create(**validated_data)

    class Meta:
        model = Pedido
        fields = '__all__'

class PedidoLotesImagenSerializer(serializers.ModelSerializer):

    items = ItemImagenSerializer(many=True)
    lotes = LoteSerializer(many = True)
    class Meta:
        model = Pedido
        fields = '__all__'
