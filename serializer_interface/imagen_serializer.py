from rest_framework import serializers

from furnipop_api.models import Imagen

class ImagenSerializer(serializers.Serializer):
    src = serializers.CharField(max_length=45, allow_blank=True, allow_null=True, required=False)

    def create(self, validated_data):

        return Imagen.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.src = validated_data.get('src',instance.src)

        instance.save()

        return instance
