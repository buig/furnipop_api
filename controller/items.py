from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from furnipop_api.models import Item, Lote, ItemsLotes, Pedido, Contenedor, ItemsPedidos, Cliente
from serializer_interface.item_serializer import ItemSerializer, ItemImagenSerializer

@api_view(['GET','POST'])
def getOrPostItem(request):
    serializer = None
    resStatus = None
    host = request.get_host()
    if(request.method =='GET'):
        q1 = Item.objects.all()
        
        serializer = ItemImagenSerializer(q1, many=True, context={'host':host})
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
    host = request.get_host()
    pk = request.query_params['pk']
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    
    if request.method == 'GET' or request.method == 'DELETE':
        serializer = ItemImagenSerializer(item, context={'host':host})
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
        items = get_lote.items.all()
        serializer = ItemSerializer(items, many=True)
        resStatus = status.HTTP_200_OK
    except Lote.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    return Response(serializer.data, status=resStatus)

@api_view(['GET','PUT','DELETE'])
def getPutDeleteItemFromLote(request):
    serializer = None
    resStatus = None
    lote_pk = request.query_params['lote_pk']
    item_pk = request.query_params['item_pk']
    try:
        lote = Lote.objects.get(pk=lote_pk)
        item = Item.objects.get(pk=item_pk)
        if request.method == 'GET' or request.method == 'DELETE':
            if lote.items.contains(item):
                resStatus = status.HTTP_200_OK
                serializer = ItemSerializer(item)
                if request.method == 'DELETE':
                    lote.items.remove(item)
            else:
                raise Item.DoesNotExist
        if request.method == 'PUT':
            if not lote.items.contains(item):
                serializer = ItemSerializer(item)
                cant = request.data.get('cantidad',1)
                ItemsLotes.objects.create(item = item, lote = lote, cantidad = cant)
            else:
                resStatus = status.HTTP_428_PRECONDITION_REQUIRED
                return Response(status=resStatus)
    except Lote.DoesNotExist or Item.DoesNotExist:
        resStatus = status.HTTP_404_NOT_FOUND
        return Response(status=resStatus)

    return Response(serializer.data, status=resStatus)

@api_view(['GET'])
def getItemsByCliente(request):
    serializer = None
    resStatus = None
    pk = request.query_params['pk']
    try:
        get_cliente = Cliente.objects.get(pk=pk)
        items = get_cliente.favoritos.all() # La variable se llama items, porque son items, pero el atributo del model Cliente se llama favoritos.
        serializer = ItemSerializer(items, many=True)
        resStatus = status.HTTP_200_OK
    except Cliente.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    return Response(serializer.data, status=resStatus)

@api_view(['GET','PUT','DELETE'])
def getPutDeleteItemFromCliente(request):
    serializer = None
    resStatus = None
    cliente_pk = request.query_params['cliente_pk']
    item_pk = request.query_params['item_pk']
    try:
        cliente = Cliente.objects.get(pk=cliente_pk)
        item = Item.objects.get(pk=item_pk)
        if request.method == 'GET' or request.method == 'DELETE':
            if cliente.favoritos.contains(item):
                resStatus = status.HTTP_200_OK
                serializer = ItemSerializer(item)
                if request.method == 'DELETE':
                    cliente.favoritos.remove(item)
            else:
                raise Item.DoesNotExist
        if request.method == 'PUT':
            if not cliente.favoritos.contains(item):
                serializer = ItemSerializer(item)
                cliente.favoritos.add(item)
            else:
                resStatus = status.HTTP_428_PRECONDITION_REQUIRED
                return Response(status=resStatus)
    except Cliente.DoesNotExist or Item.DoesNotExist:
        resStatus = status.HTTP_404_NOT_FOUND
        return Response(status=resStatus)

    return Response(serializer.data, status=resStatus)

@api_view(['GET'])
def getItemsByPedido(request):
    serializer = None
    resStatus = None
    pk = request.query_params['pk']
    try:
        get_pedido = Pedido.objects.get(pk=pk)
        items = get_pedido.items.all()
        serializer = ItemSerializer(items, many=True)
        resStatus = status.HTTP_200_OK
    except Pedido.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    return Response(serializer.data, status=resStatus)

@api_view(['GET','PUT','DELETE'])
def getPutDeleteItemFromPedido(request):
    serializer = None
    resStatus = None
    pedido_pk = request.query_params['pedido_pk']
    item_pk = request.query_params['item_pk']
    try:
        pedido = Pedido.objects.get(pk=pedido_pk)
        item = Item.objects.get(pk=item_pk)
        if request.method == 'GET' or request.method == 'DELETE':
            if pedido.items.contains(item):
                resStatus = status.HTTP_200_OK
                serializer = ItemSerializer(item)
                if request.method == 'DELETE':
                    pedido.items.remove(item)
            else:
                raise Item.DoesNotExist
        if request.method == 'PUT':
            if not pedido.items.contains(item):
                serializer = ItemSerializer(item)
                cant = request.data.get('cantidad',1)
                ItemsPedidos.objects.create(item = item, pedido = pedido, cantidad = cant)
            else:
                resStatus = status.HTTP_428_PRECONDITION_REQUIRED
                return Response(status=resStatus)
    except Pedido.DoesNotExist or Item.DoesNotExist:
        resStatus = status.HTTP_404_NOT_FOUND
        return Response(status=resStatus)

    return Response(serializer.data, status=resStatus)

@api_view(['GET'])
def getItemsByContenedor(request):
    serializer = None
    resStatus = None
    pk = request.query_params['pk']
    try:
        get_contenedor = Contenedor.objects.get(pk=pk)
        items = Item.objects.filter(contenedor=get_contenedor)
        serializer = ItemSerializer(items, many=True)
        resStatus = status.HTTP_200_OK
    except Pedido.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    return Response(serializer.data, status=resStatus)
