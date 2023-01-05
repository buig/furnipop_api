from rest_framework import serializers

from furnipop_api.models import Departamento

class DepartamentoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    nombre = serializers.CharField(max_length=45)
    codigo = serializers.CharField(max_length=45)

    def create(self, validated_data):

        return Departamento.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.codigo = validated_data.get('codigo',instance.codigo)

        instance.save()

        return instance

    class Meta:
        model = Departamento
        #fields = '__all__'
        fields = ['id','nombre','codigo']
