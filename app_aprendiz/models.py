from django.db import models

# Create your models here.
class aprendiz(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    correo = models.EmailField(unique=True)
    estado_activo = models.BooleanField(default=True)

class calificacion(models.Model):
    aprendiz = models.ForeignKey(aprendiz, related_name='notas', on_delete=models.CASCADE)
    valor = models.FloatField()

def str(self):
    return self.nombre

def str(self):
    return self.edad

def str(self):
    return self.correo

def str(self):
    return self.estado_activo

class notas(models.Model):
    nombre = models.CharField(max_length=100)
    nota1 = models.FloatField()
    nota2 = models.FloatField()
    nota3 = models.FloatField()
    nota4 = models.FloatField()

    def promedio(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

    def aprobado(self):
        return self.promedio() >= 3