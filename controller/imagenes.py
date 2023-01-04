from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from furnipop_api.models import Imagen
from serializer_interface.imagen_serializer import ImagenSerializer

@api_view(['GET','POST'])
def getOrPostImagen(request):
    serializer = None
    resStatus = None
    if(request.method =='GET'):
        q1 = Imagen.objects.all()
        
        serializer = ImagenSerializer(q1, many=True)
        resStatus = status.HTTP_200_OK
    if request.method=='POST':

        serializer = ImagenSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            resStatus = status.HTTP_201_CREATED
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(status = resStatus)

    return Response(serializer.data, status= resStatus)

@api_view(['GET', 'PUT', 'DELETE'])
def getPutDeleteImagen(request):
    serializer = None
    resStatus = None
    pk = request.query_params['pk']
    try:
        imagen = Imagen.objects.get(pk=pk)
    except Imagen.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    
    if request.method == 'GET' or request.method == 'DELETE':
        serializer = ImagenSerializer(imagen)
        resStatus = status.HTTP_200_OK
        if request.method == 'DELETE':
            resStatus = status.HTTP_204_NO_CONTENT
            imagen.delete()
    
    if request.method == 'PUT':
        serializer = ImagenSerializer(imagen, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(serializer.errors,status=resStatus)

    return Response(serializer.data, status=resStatus)