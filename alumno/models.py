from django.db import models

# Create your models here.
class Alumno(models.Model):
    

    name = models.CharField("Nombre", max_length=100, blank=False)
    email = models.EmailField("Correo Electrónico", max_length=100, blank=False)
    number_tel = models.CharField("Número Telefónico", max_length=10, blank=False)
    area = models.CharField("Área", max_length=50, blank=False)
    school = models.CharField("Escuela de procedencia", max_length=100, blank=False)
    created_at = models.DateField("Fecha de registro", auto_now=True)
    active = models.BooleanField("Alumno Activo", default=False)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = "Alumnos"
        unique_together = ['email', 'number_tel']
    
    def __str__(self):
        return f"{self.name}, ({self.email}, {self.number_tel}) -- {self.area}"

    @property
    def nombre_referencia(self):
        return f"{self.name} -- ({self.area})"