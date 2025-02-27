from rest_framework import serializers
from .models import Project 

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)
        
#  serializers.py
#Este archivo se encarga de convertir los objetos de Django (modelos) en 
# formatos JSON para que puedan ser usados en la API y viceversa.

# Explicación:
# serializers.ModelSerializer: Es una clase de DRF que simplifica la creación de serializadores.
# model = Project: Indica que este serializador se basa en el modelo Project.
# fields = (...): Define los campos del modelo que se incluirán en la API.
# ('created_at',) Esto hace que created_at sea de solo lectura.