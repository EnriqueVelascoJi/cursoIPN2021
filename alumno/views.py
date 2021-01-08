from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Alumno
from .serializers import AlumnoSerializer


@api_view(['GET'])
def alumnosOverview(request):
    api_urls = {
        'List': '/listar',
        'Create': '/crear',
    }
    return Response(api_urls)

@api_view(['GET'])
def listar_alumno(request):
    alumnos = Alumno.objects.all()
    serializer = AlumnoSerializer(alumnos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def crear_alumno(request):
    serializer = AlumnoSerializer(data = request.data)
    if  serializer.is_valid():
        serializer.save()
        email = serializer.cleaned_data['email']

    return Response(serializer.data, email)