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
from farmaceuta.models import *
from administrador.models import *
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