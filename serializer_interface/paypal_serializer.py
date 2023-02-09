from rest_framework import serializers

from furnipop_api.models import Paypal
from .metodo_pago_serializer import MetodoPagoSerializer

class PaypalSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        return Paypal.objects.create(**validated_data)


    class Meta:
        model = Paypal
        fields = '__all__'

class PaypalMetodoPagoSerializer(serializers.ModelSerializer):

    metodo_pago = MetodoPagoSerializer()


    class Meta:
        model = Paypal
        fields = '__all__'
