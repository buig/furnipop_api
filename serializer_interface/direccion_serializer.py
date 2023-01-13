from rest_framework import serializers

from furnipop_api.models import Direccion

class DireccionSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Direccion.objects.create(**validated_data)

    class Meta:
        model = Direccion
        fields = '__all__'
