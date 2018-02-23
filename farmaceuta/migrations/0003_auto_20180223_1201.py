# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmaceuta', '0002_auto_20180223_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmacia',
            name='farmaceuta',
            field=models.ForeignKey(to='farmaceuta.Farmaceuta'),
        ),
    ]
