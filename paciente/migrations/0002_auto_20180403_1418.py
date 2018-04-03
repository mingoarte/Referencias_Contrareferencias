# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0001_initial'),
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historia',
            name='especialidad',
            field=models.ForeignKey(to='medico.Especialidad', null=True),
        ),
        migrations.AddField(
            model_name='historia',
            name='medico',
            field=models.ForeignKey(to='medico.Medico', null=True),
        ),
        migrations.AddField(
            model_name='historiadetriaje',
            name='medico_triaje',
            field=models.ForeignKey(to='medico.Medico', null=True),
        ),
    ]
