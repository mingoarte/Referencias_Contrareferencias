# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmaceuta', '0004_auto_20180309_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicamento',
            name='marca',
        ),
    ]
