from django.db import models
from django.db.models import Q
from administrador.models import *
from medico.models import *
from django.core.validators import MaxValueValidator

# Create your models here.
class Farmacia(models.Model):
    
    rif = models.CharField(max_length=12, blank=False)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, blank=False)
    institucion = models.ForeignKey(Institucion,
    								limit_choices_to=Q(tipo = 'Clinica') | Q(tipo = 'Hospital'))

    def __str__(self):
        return self.name