from django.conf import settings
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Alumno
from .serializers import AlumnoSerializer

from django.core.mail import send_mail

from rest_framework.renderers import JSONRenderer


invitacion = """Enrique Velasco Jimenez is inviting you to a scheduled Zoom meeting.

Topic: Primer Sesión Informativa Curso IPN 2021
Time: Jan 16, 2021 03:00 PM Mexico City

Join Zoom Meeting
https://us04web.zoom.us/j/71277641603?pwd=L3U2ODZtTW1TVkZodjF5QUlXbXp5dz09

Meeting ID: 712 7764 1603
Passcode: Sesion1Inf


"""
def send_email(emaildes):
    
    send_mail(
        'Primer sesión informativa y confirmación de resgistro',
        f"""Gracias por tu confianza!!
        Bienvenido al Curso de Preparación para el Nivel Superior IPN 2021.
           
        Tu registro se ha completado exitosamente.
           
        Te esperamos el día Sábado 16 de Enero a nuestra primer sesión informativa, donde presentaremos el curso y daremos las indicaciones correspondientes a los pagos, fechas, grupos, horarios, etc. Aclararemos todas las dudas que se puedan presentar. Adjuntamos el link de la reunión (zoom):
        
        {invitacion}


        Saludos cordiales!!
        """,
        settings.EMAIL_HOST_USER,
        [emaildes],
        fail_silently=False,
    )

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
    email = request.data.get('email')
    if  serializer.is_valid():
        serializer.save()
        send_email(email)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)