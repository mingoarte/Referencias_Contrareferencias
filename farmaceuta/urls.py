from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from farmaceuta.views import *


urlpatterns = [
    url(
        r'^agregar-farmacia$',
        agregarFarmacia.as_view(),
        name='agregar_farmacia'
    ),
    url(
        r'^ver-farmacias$',
        verFarmacias.as_view(),
        name='ver_farmacias'
    ),
    url(
        r'^modificar-farmacia/(?P<pk>\w+)$',
        ModificarFarmacia.as_view(),
        name='modificar_farmacia'
    ),
    url(
        r'^eliminar-farmacia/(?P<pk>\w+)$',
        'farmaceuta.controllers.eliminar_farmacia',
        name='eliminar_farmacia'
    ),
    url(
        r'^perfil-farmaceuta/(?P<id>\w+)$',
        PerfilFarmaceuta.as_view(),
        name='perfil_farmaceuta'
    ),
    
]
