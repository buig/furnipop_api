from django.http import HttpResponse
from django.core import serializers

from furnipop_api.models import Color


def index(request):
    q1 = Color.objects.all()
    
    data = serializers.serialize('json', q1, fields=('nombre'))
    return HttpResponse(data)