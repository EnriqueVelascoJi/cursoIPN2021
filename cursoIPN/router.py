from alumno.viewstets import AlumnoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alumno', AlumnoViewset)
