from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from furnipop_api.models import Empleado, Departamento
from serializer_interface.empleado_serializer import EmpleadoSerializer
from serializer_interface.empleado_dept_serializer import EmpleadoDeptSerializer

@api_view(['POST'])
@permission_classes((AllowAny,))
def validateEmpleado(request):
    serializer = None
    resStatus = None
    data = request.data
    email = data['email']
    password = data['password']
    try:
        empleado = Empleado.objects.get(email=email, password = password)
    except Empleado.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)

    if (request.method == 'POST'):
        serializer = EmpleadoSerializer(empleado)
        resStatus = status.HTTP_200_OK
    
    return Response(serializer.data, status=resStatus)

@api_view(['GET','POST'])
def getOrPostEmpleado(request):
    serializer = None
    resStatus = None
    if(request.method =='GET'):
        q1 = Empleado.objects.all()
        
        serializer = EmpleadoSerializer(q1, many=True)
        resStatus = status.HTTP_200_OK
    if request.method=='POST':

        serializer = EmpleadoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            resStatus = status.HTTP_201_CREATED
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(serializer.errors,status = resStatus)

    return Response(serializer.data, status= resStatus)

@api_view(['GET', 'PUT', 'DELETE'])
def getPutDeleteEmpleado(request,pk):
    serializer = None
    resStatus = None
    #pk = request.query_params['pk']
    try:
        empleado = Empleado.objects.get(pk=pk)
    except Empleado.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    
    if request.method == 'GET' or request.method == 'DELETE':
        serializer = EmpleadoSerializer(empleado)
        resStatus = status.HTTP_200_OK
        if request.method == 'DELETE':
            resStatus = status.HTTP_204_NO_CONTENT
            empleado.delete()
    
    if request.method == 'PUT':
        serializer = EmpleadoSerializer(empleado, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(serializer.errors,status=resStatus)

    return Response(serializer.data, status=resStatus)

@api_view(['GET'])
def getEmpleadosFromDepartamento(request, pk):
    serializer = None
    resStatus = None
    #pk = request.query_params['pk']
    try:
        dept = Departamento.objects.get(pk=pk)
        q1 = Empleado.objects.filter(departamento = dept)
        serializer = EmpleadoDeptSerializer(q1, many=True)
        resStatus = status.HTTP_200_OK
    except Empleado.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)

    return Response(serializer.data, status = resStatus)

@api_view(['PUT'])
def putEmpleadoInDepartamento(request, departamento_pk, empleado_pk):
    serializer = None
    resStatus = None
    #empleado_pk = request.query_params['empleado_pk']
    #departamento_pk = request.query_params['departamento_pk']
    try:
        dept = Departamento.objects.get(pk=departamento_pk)
        emp = Empleado.objects.get(pk=empleado_pk)
        serializer = EmpleadoSerializer(emp)
        serializer.updateDept(emp,dept)
        resStatus = status.HTTP_200_OK
    except Empleado.DoesNotExist or Departamento.DoesNotExist:
        resStatus = status.HTTP_404_NOT_FOUND
        return Response(status=resStatus)

    return Response(serializer.data, status = resStatus)

