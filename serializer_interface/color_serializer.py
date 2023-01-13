from rest_framework import serializers

from furnipop_api.models import Color

class ColorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Color
        fields = '__all__'
