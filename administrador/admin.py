from django.contrib import admin
from administrador.models import *
from medico.models import *
from paciente.models import *
from farmaceuta.models import *

# Register your models here.
admin.site.register(Medico)
admin.site.register(Medico_Estudios)
admin.site.register(Medico_Logros)
admin.site.register(Institucion)
admin.site.register(Medico_Publicaciones)
admin.site.register(Paciente)
admin.site.register(Usuario)
admin.site.register(Historiadetriaje)
admin.site.register(Medico_Especialidad)
admin.site.register(Especialidad)
admin.site.register(Farmacia)
admin.site.register(RecipeMedico)
