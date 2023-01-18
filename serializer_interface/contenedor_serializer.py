from rest_framework import serializers

from furnipop_api.models import Contenedor

class ContenedorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    ubicacion = serializers.CharField(max_length=100, allow_blank=True, allow_null=True,required=False)

    class Meta:
        model = Contenedor
        fields = '__all__'
