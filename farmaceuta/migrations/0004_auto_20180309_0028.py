# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('farmaceuta', '0003_auto_20180223_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f_elaboracion', models.DateField()),
                ('f_vencimiento', models.DateField()),
                ('precio', models.DecimalField(max_digits=15, decimal_places=2)),
                ('cantidad', models.PositiveIntegerField()),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=256)),
                ('indicacion', models.TextField(max_length=512)),
                ('posologia', models.TextField(max_length=512)),
                ('marca', models.CharField(max_length=256)),
                ('stock', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('tipo', models.CharField(max_length=32, choices=[(b'inyectable', b'Inyectable'), (b'grajeas', b'Grajeas'), (b'jarabe', b'Jarabe')])),
            ],
        ),
        migrations.AlterField(
            model_name='farmacia',
            name='farmaceuta',
            field=models.ForeignKey(to='farmaceuta.Farmaceuta', null=True),
        ),
        migrations.AddField(
            model_name='medicamento',
            name='farmacia',
            field=models.ForeignKey(to='farmaceuta.Farmacia', null=True),
        ),
        migrations.AddField(
            model_name='lote',
            name='medicamento',
            field=models.ForeignKey(to='farmaceuta.Medicamento'),
        ),
    ]
