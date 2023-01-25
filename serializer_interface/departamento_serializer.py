from rest_framework import serializers

from furnipop_api.models import Departamento

class DepartamentoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Departamento
        fields = '__all__'
        #fields = ['id','nombre','codigo']
