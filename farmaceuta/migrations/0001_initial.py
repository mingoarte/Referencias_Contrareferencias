# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_auto_20180222_0139'),
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmaceuta',
            fields=[
                ('cedula', models.IntegerField(serialize=False, primary_key=True, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('first_name', models.CharField(max_length=30, null=True, blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, blank=True)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('sexo', models.CharField(max_length=10, null=True, blank=True)),
                ('estado_civil', models.CharField(max_length=15, null=True, blank=True)),
                ('telefono', models.CharField(max_length=15, null=True, blank=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('usuario', models.ForeignKey(to='administrador.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Farmacia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rif', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('farmaceuta', models.OneToOneField(default=24211328, to='farmaceuta.Farmaceuta')),
                ('institucion', models.ForeignKey(blank=True, to='medico.Institucion', null=True)),
            ],
        ),
    ]
