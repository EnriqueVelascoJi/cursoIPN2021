from rest_framework import viewsets

from . import models
from . import serializers

class AlumnoViewset(viewsets.ModelViewSet):
    queryset = models.Alumno.objects.all()
    serializer_class = serializers.AlumnoSerializer