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
        fields = ['nombre','direccion', 'rif','institucion']

