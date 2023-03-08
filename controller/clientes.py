from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from furnipop_api.models import Cliente
from serializer_interface.cliente_serializer import ClienteSerializer

@api_view(['POST'])
@permission_classes((AllowAny,))
def validateCliente(request):
    serializer = None
    resStatus = None
    data = request.data
    email = data['email']
    password = data['password']
    try:
        cliente = Cliente.objects.get(email=email, password = password)
    except Cliente.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)

    if (request.method == 'POST'):
        serializer = ClienteSerializer(cliente)
        resStatus = status.HTTP_200_OK
    
    return Response(serializer.data, status=resStatus)

@api_view(['GET','POST'])
def getOrPostCliente(request):
    serializer = None
    resStatus = None
    if(request.method =='GET'):
        q1 = Cliente.objects.all()
        
        serializer = ClienteSerializer(q1, many=True)
        resStatus = status.HTTP_200_OK

    if request.method=='POST':
        serializer = ClienteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            resStatus = status.HTTP_201_CREATED
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(status = resStatus)

    return Response(serializer.data, status= resStatus)

@api_view(['GET', 'PUT', 'DELETE'])
def getPutDeleteCliente(request,pk):
    serializer = None
    resStatus = None
    #pk = request.query_params['pk']
    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    
    if request.method == 'GET' or request.method == 'DELETE':
        serializer = ClienteSerializer(cliente)
        resStatus = status.HTTP_200_OK
        if request.method == 'DELETE':
            resStatus = status.HTTP_204_NO_CONTENT
            cliente.delete()
    
    if request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(serializer.errors,status=resStatus)

    return Response(serializer.data, status=resStatus)
