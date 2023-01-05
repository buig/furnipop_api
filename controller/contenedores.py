from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from furnipop_api.models import Contenedor
from serializer_interface.contenedor_serializer import ContenedorSerializer

@api_view(['GET','POST'])
def getOrPostContenedor(request):
    serializer = None
    resStatus = None
    if(request.method =='GET'):
        q1 = Contenedor.objects.all()
        
        serializer = ContenedorSerializer(q1, many=True)
        resStatus = status.HTTP_200_OK
    if request.method=='POST':

        serializer = ContenedorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            resStatus = status.HTTP_201_CREATED
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(serializer.errors, status = resStatus)

    return Response(serializer.data, status= resStatus)

@api_view(['GET', 'PUT', 'DELETE'])
def getPutDeleteContenedor(request):
    serializer = None
    resStatus = None
    pk = request.query_params['pk']
    try:
        contenedor = Contenedor.objects.get(pk=pk)
    except Contenedor.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    
    if request.method == 'GET' or request.method == 'DELETE':
        serializer = ContenedorSerializer(contenedor)
        resStatus = status.HTTP_200_OK
        if request.method == 'DELETE':
            resStatus = status.HTTP_204_NO_CONTENT
            contenedor.delete()
    
    if request.method == 'PUT':
        serializer = ContenedorSerializer(contenedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(serializer.errors,status=resStatus)

    return Response(serializer.data, status=resStatus)