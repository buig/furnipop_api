from rest_framework import serializers

from furnipop_api.models import Tarjeta
from .metodo_pago_serializer import MetodoPagoSerializer

class TarjetaSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        return Tarjeta.objects.create(**validated_data)

    class Meta:
        model = Tarjeta
        fields = '__all__'

class TarjetaMetodoPagoSerializer(serializers.ModelSerializer):

    metodo_pago = MetodoPagoSerializer()

    class Meta:
        model = Tarjeta
        fields = '__all__'