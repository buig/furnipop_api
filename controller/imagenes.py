from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from pathlib import Path

from furnipop_api.models import Imagen
from serializer_interface.imagen_serializer import ImagenSerializer

@api_view(['GET','POST'])
def getOrPostImagen(request):
    serializer = None
    resStatus = None
    host = request.get_host()
    if(request.method =='GET'):
        q1 = Imagen.objects.all()
        
        serializer = ImagenSerializer(q1, many=True, context={'host':host})
        resStatus = status.HTTP_200_OK
    if request.method=='POST':

        serializer = ImagenSerializer(data = request.data, context={'host':host})
        #file = request.data['src']
        #img = Imagen(src=file)
        #serializer = ImagenSerializer(img)
        if serializer.is_valid():
            serializer.save()
            resStatus = status.HTTP_201_CREATED
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(status = resStatus)

    return Response(serializer.data, status= resStatus)

@api_view(['GET', 'DELETE'])
def getPutDeleteImagen(request):
    serializer = None
    resStatus = None
    host = request.get_host()
    pk = request.query_params['pk']
    try:
        imagen = Imagen.objects.get(pk=pk)
    except Imagen.DoesNotExist:
            resStatus = status.HTTP_404_NOT_FOUND
            return Response(status=resStatus)
    
    if request.method == 'GET' or request.method == 'DELETE':
        serializer = ImagenSerializer(imagen, context={'host':host})
        resStatus = status.HTTP_200_OK
        if request.method == 'DELETE':
            resStatus = status.HTTP_204_NO_CONTENT
            remove_img_file(imagen)
            imagen.delete()
    
    if request.method == 'PUT':
        serializer = ImagenSerializer(imagen, data=request.data, context={'host':host})
        remove_img_file(imagen)
        if serializer.is_valid():
            serializer.save()
        else:
            resStatus = status.HTTP_400_BAD_REQUEST
            return Response(serializer.errors,status=resStatus)

    return Response(serializer.data, status=resStatus)

def remove_img_file(imagen):
    parent_path = Path(__file__).parent.parent
    imgFile = imagen.src.url
    if imgFile[0] == '/':
        imgFile = imgFile[1:]
    file = parent_path.joinpath(imgFile)
    file.unlink()