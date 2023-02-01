from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from furnipop_api.models import Lote, Pedido, Item, LotesPedidos
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

@api_view(['GET'])
def getLotesByPedido(request):
    serializer = None
    resStatus = None
    pk = request.query_params['pk']
    try:
        get_pedido = Pedido.objects.get(pk=pk)
        lotes = get_pedido.lotes.all()
        serializer = LoteSerializer(lotes, many=True)
        resStatus = status.HTTP_200_OK
    except Pedido.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    return Response(serializer.data, status=resStatus)

@api_view(['GET','PUT','DELETE'])
def getPutDeleteLoteFromPedido(request):
    serializer = None
    resStatus = None
    pedido_pk = request.query_params['pedido_pk']
    lote_pk = request.query_params['lote_pk']
    try:
        pedido = Pedido.objects.get(pk=pedido_pk)
        lote = Lote.objects.get(pk=lote_pk)
        if request.method == 'GET' or request.method == 'DELETE':
            if pedido.lotes.contains(lote):
                resStatus = status.HTTP_200_OK
                serializer = LoteSerializer(lote)
                if request.method == 'DELETE':
                    pedido.lotes.remove(lote)
            else:
                raise Lote.DoesNotExist
        if request.method == 'PUT':
            if not pedido.lotes.contains(lote):
                serializer = LoteSerializer(lote)
                LotesPedidos.objects.create(lote = lote, pedido = pedido)
            else:
                resStatus = status.HTTP_428_PRECONDITION_REQUIRED
                return Response(status=resStatus)
    except Pedido.DoesNotExist or Lote.DoesNotExist:
        resStatus = status.HTTP_404_NOT_FOUND
        return Response(status=resStatus)

    return Response(serializer.data, status=resStatus)
