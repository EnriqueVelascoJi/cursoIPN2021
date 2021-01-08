from django.urls import  path
from . import views

app_name = 'alumno_app'
urlpatterns = [
    path('', views.alumnosOverview, name="api-overview"),
    path('listar/', views.listar_alumno, name="listar_alumnos"),
    path('crear/', views.crear_alumno, name="crear-alumno")
]