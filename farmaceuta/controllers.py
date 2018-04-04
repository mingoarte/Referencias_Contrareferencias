from administrador.models import *
from farmaceuta.models import *
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
import parsedatetime as pdt


def editar_farmaceuta(user, nombre, apellido, email, sexo, fecha, estado_civil,
                      telefono, direccion, foto):
    try:
        usuario = Usuario.objects.get(user=user)
        user = User.objects.get(pk=usuario.user.pk)
        farmaceuta = Farmaceuta.objects.get(usuario=usuario)
        farmaceuta.first_name = nombre
        user.first_name = nombre
        farmaceuta.last_name = apellido
        user.last_name = apellido
        farmaceuta.email = email
        user.email = email
        farmaceuta.sexo = sexo
        try:
            fecha = datetime.datetime.strptime(fecha,
                                               '%d-%m-%Y'
                                               ).strftime('%Y-%m-%d')
        except:
            if fecha is None:
                fecha = None
            else:
                cal = pdt.Calendar()
                now = datetime.datetime.now()
                fecha = cal.parseDT(fecha, now)[0]

        farmaceuta.fecha_nacimiento = fecha
        farmaceuta.estado_civil = estado_civil
        farmaceuta.telefono = telefono
        farmaceuta.direccion = direccion
        print("fotooooooooooooooo")
        print(foto == False)
        if foto != False :
            usuario.foto=foto
            usuario.fotosubida = True
        usuario.save()
        farmaceuta.save()
        user.save()
        return True

    except:
        return False


def modificar_farmacia(inst_id, direccion, institucion, farmaceuta):
    try:
        farmacia = Farmacia.objects.get(pk=int(inst_id))
        farmacia.direccion = direccion
        if institucion:
            institucion = Institucion.objects.get(id=institucion)
            farmacia.institucion = institucion
        if farmaceuta:
            farmaceuta = Farmaceuta.objects.get(cedula=farmaceuta)
            farmacia.farmaceuta = farmaceuta
        farmacia.save()
        return True
    except:
        return False


def eliminar_farmacia(request, pk):
    farmacia = Farmacia.objects.get(pk=pk)
    farmacia.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_farmacias'))

def eliminar_medicamento(request, pk, farmacia):
    medicamento = Medicamento.objects.get(pk=pk)
    medicamento.delete()
    return HttpResponseRedirect(reverse_lazy('ver_medicamentos', kwargs={'pk': farmacia}))