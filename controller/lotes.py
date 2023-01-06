from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from furnipop_api.models import Lote
from serializer_interface.lote_serializer import LoteSerializer

@api_view(['GET','POST'])
def getOrPostLote(request):
    serializer = None
    resStatus = None
    if(request.method =='GET'):
        q1 = Lote.objects.all()
        
        serializer = LoteSerializer(q1, many=True)
        resStatus = status.HTTP_200_OK
    if request.method=='POST':

        serializer = LoteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            resStatus = status.HTTP_201_CREATED
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(status = resStatus)

    return Response(serializer.data, status= resStatus)

@api_view(['GET', 'PUT', 'DELETE'])
def getPutDeleteLote(request):
    serializer = None
    resStatus = None
    pk = request.query_params['pk']
    try:
        lote = Lote.objects.get(pk=pk)
    except Lote.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    
    if request.method == 'GET' or request.method == 'DELETE':
        serializer = LoteSerializer(lote)
        resStatus = status.HTTP_200_OK
        if request.method == 'DELETE':
            resStatus = status.HTTP_204_NO_CONTENT
            lote.delete()
    
    if request.method == 'PUT':
        serializer = LoteSerializer(lote, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(serializer.errors,status=resStatus)

    return Response(serializer.data, status=resStatus)