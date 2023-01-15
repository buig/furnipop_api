from rest_framework import serializers

from furnipop_api.models import Imagen

class ImagenSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    src = serializers.CharField(max_length=45, allow_blank=True, allow_null=True, required=False)


    def update(self, instance, validated_data):

        instance.src = validated_data.get('src',instance.src)

        instance.save()

        return instance

    class Meta:
        model = Imagen
        fields = '__all__'