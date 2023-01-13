from rest_framework import serializers

from furnipop_api.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        return Cliente.objects.create(**validated_data)

    class Meta:
        model = Cliente
        fields = '__all__'
