from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Alumno
from .serializers import AlumnoSerializer


@api_view(['GET', 'POST'])
def alumnos_list(request):
    """
    List all code alumnserializer = AlumnoSerializer(alumnos, or create a new snippet.
    """
    if request.method == 'GET':
        alumnos = alumnos.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlumnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)