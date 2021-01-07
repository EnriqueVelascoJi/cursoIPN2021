from django.contrib import admin
from .models import Alumno
# Register your models here.
@admin.register(Alumno)

class AlumnoAdmin(admin.ModelAdmin):

    ordering = ["id"]

    list_display = (
        'id',
        'name',
        'email',
        'number_tel',
        'area',
        'school',
        'created_at',
        'active',
        'nombre_referencia',
    )

    list_filter = (
        'area',
    )
    search_fields = (
        '__all__',
    )
