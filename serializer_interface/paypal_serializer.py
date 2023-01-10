from rest_framework import serializers

from furnipop_api.models import Paypal

class PaypalSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=45)
    metodo_pago_id = serializers.IntegerField()

    def create(self, validated_data):

        return Paypal.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.email = validated_data.get('email',instance.email)
        instance.metodo_pago_id = validated_data.get('metodo_pago_id',instance.metodo_pago_id)

        instance.save()

        return instance