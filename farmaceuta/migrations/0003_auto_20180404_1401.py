# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmaceuta', '0002_medicamento_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='marca',
            field=models.ForeignKey(default=1, to='medico.Institucion'),
            preserve_default=False,
        ),
    ]
