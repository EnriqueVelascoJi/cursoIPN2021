from django.urls import  path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.alumnosOverview, name="api-overview"),
    path('listar/', views.listar_alumno, name="listar_alumnos"),
    path('crear/', views.crear_alumno, name="crear-alumno")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
