from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializers

class ProjectViewSet(viewsets.ModelViewSet):
    queryset =  Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializers
    
#api.py
# Este archivo define la vista de la API, permitiendo interactuar con los datos.

# Explicación:
# viewsets.ModelViewSet: Proporciona las operaciones CRUD (GET, POST, PUT, DELETE) automáticamente.
# queryset = Project.objects.all(): Recupera todos los registros de Project.
# permission_classes = [permissions.AllowAny]: Permite que cualquier usuario acceda a esta API.
# serializer_class = ProjectSerializers: Usa el serializador definido en serializers.py para manejar los datos.