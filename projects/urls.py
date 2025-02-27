from rest_framework import routers 
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls

#urls.py
# Este archivo define las rutas de la API.

# Explicación:
#routers.DefaultRouter(): Crea un router para manejar las rutas de la API automáticamente.
# router.register('api/projects', ProjectViewSet, 'projects'):
# Registra la vista ProjectViewSet bajo la ruta api/projects/.
# urlpatterns = router.urls: Asigna las rutas generadas por el router a urlpatterns, para que Django las reconozca.