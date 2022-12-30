from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Color


def index(request):
    q1 = Color.objects.all().values()
    
    data = dict()

    for value in q1:
        id = value['id']
        word = value['nombre']
        data[id] = word

    return JsonResponse(data, safe=False)