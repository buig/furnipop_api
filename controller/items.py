from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from furnipop_api.models import Item, Lote, ItemsLotes
from serializer_interface.item_serializer import ItemSerializer

@api_view(['GET','POST'])
def getOrPostItem(request):
    serializer = None
    resStatus = None
    if(request.method =='GET'):
        q1 = Item.objects.all()
        
        serializer = ItemSerializer(q1, many=True)
        resStatus = status.HTTP_200_OK
    if request.method=='POST':

        serializer = ItemSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            resStatus = status.HTTP_201_CREATED
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(status = resStatus)

    return Response(serializer.data, status= resStatus)

@api_view(['GET', 'PUT', 'DELETE'])
def getPutDeleteItem(request):
    serializer = None
    resStatus = None
    pk = request.query_params['pk']
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    
    if request.method == 'GET' or request.method == 'DELETE':
        serializer = ItemSerializer(item)
        resStatus = status.HTTP_200_OK
        if request.method == 'DELETE':
            resStatus = status.HTTP_204_NO_CONTENT
            item.delete()
    
    if request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(serializer.errors,status=resStatus)

    return Response(serializer.data, status=resStatus)

@api_view(['GET'])
def getItemsByLote(request):
    serializer = None
    resStatus = None
    pk = request.query_params['pk']
    try:
        get_lote = Lote.objects.get(pk=pk)
        itemsLotes = ItemsLotes.objects.filter(lote=get_lote)
        itemList = list()
        for iLote in itemsLotes:
            itemList.append(iLote.item)
        serializer = ItemSerializer(itemList, many=True)
        resStatus = status.HTTP_200_OK
    except Lote.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    return Response(serializer.data, status=resStatus)