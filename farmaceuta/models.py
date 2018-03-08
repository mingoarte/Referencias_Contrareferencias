from django.db import models
from django.db.models import Q
from administrador.models import *
from medico.models import *
from django.core.validators import MaxValueValidator

# Create your models here.
class Farmaceuta(models.Model):
    cedula = models.IntegerField(primary_key=True,
                                 validators=[MaxValueValidator(99999999)])
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    estado_civil = models.CharField(max_length=15, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.ForeignKey(Usuario,
                                on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cedula) + " " + self.first_name + " " + self.last_name


class Farmacia(models.Model):
    
    rif = models.CharField(max_length=12, blank=False)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, blank=False)
    institucion = models.ForeignKey(Institucion,
    								limit_choices_to=Q(tipo = 'Clinica') | Q(tipo = 'Hospital'),
    								null=True,
    								blank=True)
    farmaceuta = models.ForeignKey(Farmaceuta, null=True)

    def __str__(self):
        return self.nombre


class Medicamento(models.Model):
    nombre = models.CharField(max_length=256, blank=False)
    indicacion = models.TextField(max_length=512, blank=False)
    posologia = models.TextField(max_length=512, blank=False)
    marca = models.CharField(max_length=256)
    stock = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(99999999)])
    tipo = models.CharField(max_length=32, choices={('grajeas', 'Grajeas'),
                                                    ('jarabe', 'Jarabe'),
                                                    ('inyectable', 'Inyectable')})
    farmacia = models.ForeignKey(Farmacia, null=True)


class Lote(models.Model):
    medicamento = models.ForeignKey(Medicamento)
    f_elaboracion = models.DateField()
    f_vencimiento = models.DateField()
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    activo = models.BooleanField()
