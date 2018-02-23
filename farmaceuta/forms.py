#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User, Group
from medico.models import *
from administrador.models import Usuario
from farmaceuta.models import *
import datetime



class farmacia_form(forms.ModelForm):
    class Meta:
        model = Farmacia
        fields = ['nombre','direccion', 'rif','institucion','farmaceuta']
	def __init__(self, *args, **kwargs):
		super(farmacia_form, self).__init__(*args, **kwargs)
		self.fields['institucion'].required = False


class FarmaciaFormEditar(forms.ModelForm):

    class Meta:
        model = Farmacia
        exclude = ["rif","nombre"]

    def __init__(self, *args, **kwargs):
    	super(FarmaciaFormEditar, self).__init__(*args, **kwargs)
    	self.fields['institucion'].empty_label = None

    # def clean_farmaceuta():