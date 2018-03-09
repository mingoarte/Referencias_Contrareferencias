# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_auto_20180222_0139'),
        ('farmaceuta', '0005_remove_medicamento_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='marca',
            field=models.ForeignKey(to='medico.Institucion', null=True),
        ),
    ]
