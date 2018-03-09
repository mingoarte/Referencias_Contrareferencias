# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmaceuta', '0007_auto_20180309_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmacia',
            name='farmaceuta',
            field=models.ForeignKey(blank=True, to='farmaceuta.Farmaceuta', null=True),
        ),
    ]
