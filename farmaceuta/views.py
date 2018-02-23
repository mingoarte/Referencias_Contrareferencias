#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth import *
from django.contrib import messages
from django.views.generic import *
from farmaceuta.forms import *
from farmaceuta.controllers import *
from farmaceuta.models import *
from administrador.models import *
from administrador.forms import *
import datetime
import calendar
import parsedatetime as pdt
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.lib.enums  import *
from io import BytesIO



class verFarmacias(TemplateView):
    template_name = 'administrador/ver_farmacias.html'

    def get_context_data(self, **kwargs):
        context = super(
            verFarmacias, self).get_context_data(**kwargs)

        farmacias = Farmacia.objects.all()
        context['farmacias'] = farmacias
        return context


class agregarFarmacia(TemplateView):
    template_name = 'administrador/agregar_farmacia.html'

    def get_context_data(self, **kwargs):
        context = super(
            agregarFarmacia, self).get_context_data(**kwargs)

        context['form'] = farmacia_form
        context['title'] = 'Agregar'

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = farmacia_form(request.POST)
        if form.is_valid():
            rif = request.POST['rif']
            nombre = request.POST['nombre']
            direccion = request.POST['direccion']
            institucion = request.POST['institucion']
            farmaceuta = request.POST['farmaceuta']

            try:
                tmp = Institucion.objects.get(pk=int(institucion))
                tmp2 = Farmaceuta.objects.get(pk=int(farmaceuta))
                value = Farmacia(rif=rif, nombre=nombre, direccion=direccion, institucion=tmp, farmaceuta=tmp2)
            except:
                value = Farmacia(rif=rif, nombre=nombre, direccion=direccion)
            
            try:
                value.save()
                return HttpResponseRedirect(reverse_lazy(
                    'ver_farmacias'))
            except:
                return render_to_response('administrador/agregar_farmacia.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            messages.error(request,"Por favor verifique los campos suguientes:")
            return render_to_response('administrador/agregar_farmacia.html',
                                      {'form': form,
                                       'title': 'Agregar'},
                                      context_instance=RequestContext(request))


class ModificarFarmacia(CreateView):
    template_name = 'administrador/modificar_farmacia.html'
    form_class = FarmaciaFormEditar

    def get_context_data(self, **kwargs):
        context = super(
            ModificarFarmacia, self).get_context_data(**kwargs)
        farmacia = Farmacia.objects.get(pk=self.kwargs['pk'])
        form = FarmaciaFormEditar(
                    initial={
                             'direccion': farmacia.direccion,
                             'institucion': farmacia.institucion,
                             'farmaceuta': farmacia.farmaceuta,
                            }
                )

        context['form'] = form
        context['farmacia'] = farmacia

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = FarmaciaFormEditar(request.POST)
        if form.is_valid():
            print('entro es valido')
            direccion = request.POST['direccion']
            institucion = request.POST['institucion']
            farmaceuta = request.POST['farmaceuta']
            value = modificar_farmacia(self.kwargs['pk'], direccion, institucion, farmaceuta)

            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'ver_farmacias'))
            else:
                return render_to_response('administrador/modificar_farmacia.html',
                                          {'form': form,
                                           'title': 'Modificar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            print('no es valido')
            return render_to_response('administrador/modificar_farmacia.html',
                                      {'form': form,
                                       'title': 'Modificar'},
                                      context_instance=RequestContext(request))


class PerfilFarmaceuta(CreateView):
    template_name = 'medico/perfil_medico.html'
    form_class = PerfilForm

    def get_context_data(self, **kwargs):
        context = super(
            PerfilFarmaceuta, self).get_context_data(**kwargs)
        user = self.request.user
        usuario = Usuario.objects.get(user=user)
        try:
            farmaceuta = Farmaceuta.objects.get(usuario=usuario)
        except:
            farmaceuta = Farmaceuta(cedula=usuario.ci, first_name=user.first_name,
                            last_name=user.last_name, fecha_nacimiento=None,
                            sexo='', estado_civil='', telefono='',
                            direccion='', usuario=usuario, foto = None)
            farmaceuta.save()
        data = {'first_name': farmaceuta.usuario.user.first_name,
                'last_name': farmaceuta.usuario.user.last_name,
                'email': farmaceuta.usuario.user.email}
        form = UsuarioForm(initial=data)
        context['usuario'] = usuario
        context['farmaceuta'] = farmaceuta
        context['form'] = form
        return context


    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = UsuarioForm(request.POST, request.FILES)
        form.fields['username'].required = False
        form.fields['passw'].required = False
        form.fields['ci'].required = False
        form.fields['rol'].required = False
        #form.fields['foto'].required = False
        print("for valido")
        print(form.is_valid())
        if form.is_valid():
            nombre = request.POST['first_name']
            apellido = request.POST['last_name']
            email = request.POST['email']
            sexo = request.POST['sex']
            fecha = request.POST['birth_date']
            estado_civil = request.POST['marital_status']
            telefono = request.POST['phone']
            direccion = request.POST['address']
            print(request.FILES=={})
            if (request.FILES!={}):
                foto = request.FILES['image']
                print("en tryyyy")
            else:
                foto = False
                print("exceptttttt")
            print("ESTA ES LA FOTO")
            #print(foto)
            value = editar_farmaceuta(request.user, nombre, apellido, email, sexo,
                                  fecha, estado_civil, telefono, direccion, foto)

            print(value)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_farmaceuta', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/perfil_medico.html',
                                          {'form': form},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/perfil_medico.html',
                                      {'form': form},
                                      context_instance=RequestContext(request))