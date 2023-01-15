from rest_framework import serializers

from furnipop_api.models import Material

class MaterialSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    nombre = serializers.CharField(max_length=45)

    def create(self, validated_data):

        return Material.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.nombre = validated_data.get('nombre',instance.nombre)

        instance.save()

        return instance

    class Meta:
        model = Material
        fields = '__all__'
