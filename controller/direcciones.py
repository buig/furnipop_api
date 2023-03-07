from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from furnipop_api.models import Direccion
from serializer_interface.direccion_serializer import DireccionSerializer

@api_view(['GET','POST'])
def getOrPostdireccion(request):
    serializer = None
    resStatus = None
    if(request.method =='GET'):
        q1 = Direccion.objects.all()
        
        serializer = DireccionSerializer(q1, many=True)
        resStatus = status.HTTP_200_OK

    if request.method=='POST':
        serializer = DireccionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            resStatus = status.HTTP_201_CREATED
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(status = resStatus)

    return Response(serializer.data, status= resStatus)

@api_view(['GET', 'PUT', 'DELETE'])
def getPutDeleteDireccion(request,pk):
    serializer = None
    resStatus = None
    #pk = request.query_params['pk']
    try:
        cliente = Direccion.objects.get(pk=pk)
    except Direccion.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    
    if request.method == 'GET' or request.method == 'DELETE':
        serializer = DireccionSerializer(cliente)
        resStatus = status.HTTP_200_OK
        if request.method == 'DELETE':
            resStatus = status.HTTP_204_NO_CONTENT
            cliente.delete()
    
    if request.method == 'PUT':
        serializer = DireccionSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(serializer.errors,status=resStatus)

    return Response(serializer.data, status=resStatus)