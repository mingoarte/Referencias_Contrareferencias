# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmaceuta', '0006_medicamento_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='farmacia',
            field=models.ForeignKey(to='farmaceuta.Farmacia'),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='marca',
            field=models.ForeignKey(to='medico.Institucion'),
        ),
    ]
