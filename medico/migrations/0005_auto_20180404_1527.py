# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0004_auto_20180404_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemedico',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 4, 4, 15, 27, 53, 83245, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
