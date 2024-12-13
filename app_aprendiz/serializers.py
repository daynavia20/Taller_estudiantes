from rest_framework import serializers
from .models import aprendiz, calificacion

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = calificacion
        fields = ['id', 'valor']

class AprendizSerializer(serializers.ModelSerializer):
    notas = CalificacionSerializer(many=True, read_only=True)

    class Meta:
        model = aprendiz
        fields = ['id', 'nombre', 'edad', 'correo', 'estado_activo', 'notas']