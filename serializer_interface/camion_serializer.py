from rest_framework import serializers

from furnipop_api.models import Camion

class CamionSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        return Camion.objects.create(**validated_data)

    class Meta:
        model = Camion
        fields = '__all__'
