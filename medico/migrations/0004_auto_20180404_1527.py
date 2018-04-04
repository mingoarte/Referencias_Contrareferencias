# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_auto_20180404_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipemedico',
            name='fecha',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='recipemedico',
            name='indicaciones',
            field=models.TextField(default=datetime.datetime(2018, 4, 4, 15, 27, 28, 952411, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
    ]
