from rest_framework import serializers

from furnipop_api.models import EstadoPedido

class EstadoPedidoSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        return EstadoPedido.objects.create(**validated_data)

    class Meta:
        model = EstadoPedido
        fields = '__all__'
