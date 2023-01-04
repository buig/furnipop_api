from rest_framework import serializers

from furnipop_api.models import Color

class ColorSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=45)

    def create(self, validated_data):

        return Color.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.nombre = validated_data.get('nombre',instance.nombre)

        instance.save()

        return instance
