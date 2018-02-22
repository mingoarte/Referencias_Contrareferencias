from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from farmaceuta.views import *


urlpatterns = [
    url(
        r'^agregar-farmacia$',
        agregarFarmacia.as_view(),
        name='agregarFarmacia'
    ),
    url(
        r'^ver-farmacias$',
        verFarmacias.as_view(),
        name='ver_farmacias'
    ),
    
]
