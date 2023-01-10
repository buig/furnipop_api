from rest_framework import serializers

from furnipop_api.models import Camion

class CamionSerializer(serializers.Serializer):
    matricula = serializers.CharField(max_length=10)

    def create(self, validated_data):

        return Camion.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.matricula = validated_data.get('matricula',instance.matricula)
        instance.save()

        return instance