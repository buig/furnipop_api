from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from furnipop_api.models import Paypal
from serializer_interface.paypal_serializer import PaypalSerializer

@api_view(['GET'])
def getPaypal(request):
    serializer = None
    resStatus = None
    if(request.method =='GET'):
        q1 = Paypal.objects.all()
        
        serializer = PaypalSerializer(q1, many=True)
        resStatus = status.HTTP_200_OK

    return Response(serializer.data, status= resStatus)

@api_view(['GET', 'PUT', 'DELETE'])
def getPutDeletePaypal(request):
    serializer = None
    resStatus = None
    pk = request.query_params['pk']
    try:
        cliente = Paypal.objects.get(pk=pk)
    except Paypal.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    
    if request.method == 'GET' or request.method == 'DELETE':
        serializer = PaypalSerializer(cliente)
        resStatus = status.HTTP_200_OK
        if request.method == 'DELETE':
            resStatus = status.HTTP_204_NO_CONTENT
            cliente.delete()
    
    if request.method == 'PUT':
        serializer = PaypalSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(serializer.errors,status=resStatus)

    return Response(serializer.data, status=resStatus)