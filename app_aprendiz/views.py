from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import aprendiz, calificacion
from .serializers import AprendizSerializer, CalificacionSerializer
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Create your views here.

class AprendizViewSet(viewsets.ModelViewSet):
    queryset = aprendiz.objects.all()
    serializer_class = AprendizSerializer

    @action(detail=True, methods=['post'])
    def añadir_nota(self, request, pk=None):
        aprendiz = self.get_object()
        nota = request.data.get('valor')
        if nota:
            calificacion.objects.create(aprendiz=aprendiz, valor=float(nota))
            return Response({'message': 'Nota agregada correctamente'})
        return Response({'error': 'Debe enviar una nota'}, status=400)

    @action(detail=True, methods=['get'])
    def aprobacion(self, request, pk=None):
        aprendiz = self.get_object()
        notas = aprendiz.notas.all()
        promedio = sum(n.valor for n in notas) / len(notas) if notas else 0
        aprobado = promedio >= 3.0
        return Response({'promedio': promedio, 'aprobado': aprobado})

    def aprendices(request, id):
        aprendiz = get_object_or_404(aprendiz, pk=id)
        return render(request, 'aprendices/aprendices.html', {'aprendiz': aprendiz})