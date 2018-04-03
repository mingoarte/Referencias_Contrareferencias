# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0001_initial'),
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
                ('farmaceuta', models.ForeignKey(blank=True, to='farmaceuta.Farmaceuta', null=True)),
                ('institucion', models.ForeignKey(blank=True, to='medico.Institucion', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('farmacia', models.ForeignKey(to='farmaceuta.Farmacia', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f_elaboracion', models.DateField()),
                ('f_vencimiento', models.DateField()),
                ('precio', models.DecimalField(max_digits=15, decimal_places=2)),
                ('cantidad', models.PositiveIntegerField()),
                ('activo', models.BooleanField(default=False)),
                ('inventario', models.ForeignKey(to='farmaceuta.Inventario', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=256)),
                ('indicacion', models.TextField(max_length=512)),
                ('posologia', models.TextField(max_length=512)),
                ('tipo', models.CharField(max_length=32, choices=[(b'inyectable', b'Inyectable'), (b'grajeas', b'Grajeas'), (b'jarabe', b'Jarabe')])),
            ],
        ),
        migrations.AddField(
            model_name='inventario',
            name='medicamento',
            field=models.ForeignKey(to='farmaceuta.Medicamento', null=True),
        ),
    ]
