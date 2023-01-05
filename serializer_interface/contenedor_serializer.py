from rest_framework import serializers

from furnipop_api.models import Contenedor

class ContenedorSerializer(serializers.Serializer):
    referencia = serializers.CharField(max_length=45)
    fecha_alta = serializers.DateTimeField()
    ubicacion = serializers.CharField(max_length=100, allow_blank=True, allow_null=True,required=False)

    def create(self, validated_data):

        return Contenedor.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.referencia = validated_data.get('referencia',instance.referencia)
        instance.fecha_alta = validated_data.get('fecha_alta',instance.fecha_alta)
        instance.ubicacion = validated_data.get('ubicacion',instance.ubicacion)

        instance.save()

        return instance
