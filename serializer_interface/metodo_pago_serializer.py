from rest_framework import serializers

from furnipop_api.models import MetodoPago

class MetodoPagoSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        return MetodoPago.objects.create(**validated_data)


    class Meta:
        model = MetodoPago
        fields = '__all__'
