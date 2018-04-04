# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_auto_20180404_1342'),
        ('farmaceuta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='marca',
            field=models.ForeignKey(to='medico.Institucion', null=True),
        ),
    ]
