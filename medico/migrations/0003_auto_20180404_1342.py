# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_recipemedico_medicamentos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipemedico',
            name='informe',
        ),
        migrations.AddField(
            model_name='recipemedico',
            name='medico',
            field=models.ForeignKey(to='medico.Medico', null=True),
        ),
    ]
