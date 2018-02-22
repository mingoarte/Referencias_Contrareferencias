# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
        ('medico', '0001_initial'),
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencia',
            name='paciente',
            field=models.ForeignKey(to='paciente.Paciente'),
        ),
        migrations.AddField(
            model_name='medico_publicaciones',
            name='medico',
            field=models.ForeignKey(to='medico.Medico'),
        ),
        migrations.AddField(
            model_name='medico_logros',
            name='medico',
            field=models.ForeignKey(to='medico.Medico'),
        ),
        migrations.AddField(
            model_name='medico_habilidades',
            name='medico',
            field=models.ForeignKey(to='medico.Medico'),
        ),
        migrations.AddField(
            model_name='medico_experiencias',
            name='medico',
            field=models.ForeignKey(to='medico.Medico'),
        ),
        migrations.AddField(
            model_name='medico_eventos',
            name='medico',
            field=models.ForeignKey(to='medico.Medico'),
        ),
        migrations.AddField(
            model_name='medico_estudios',
            name='medico',
            field=models.ForeignKey(to='medico.Medico'),
        ),
        migrations.AddField(
            model_name='medico_especialidad',
            name='especialidad',
            field=models.ForeignKey(to='medico.Especialidad'),
        ),
        migrations.AddField(
            model_name='medico_especialidad',
            name='institucion',
            field=models.ForeignKey(to='medico.Institucion'),
        ),
        migrations.AddField(
            model_name='medico_especialidad',
            name='medico',
            field=models.ForeignKey(to='medico.Medico'),
        ),
        migrations.AddField(
            model_name='medico_citas',
            name='especialidad',
            field=models.ForeignKey(to='medico.Especialidad'),
        ),
        migrations.AddField(
            model_name='medico_citas',
            name='institucion',
            field=models.ForeignKey(to='medico.Institucion'),
        ),
        migrations.AddField(
            model_name='medico_citas',
            name='medico',
            field=models.ForeignKey(to='medico.Medico'),
        ),
        migrations.AddField(
            model_name='medico_citas',
            name='paciente',
            field=models.ForeignKey(to='paciente.Paciente'),
        ),
        migrations.AddField(
            model_name='medico',
            name='usuario',
            field=models.ForeignKey(to='administrador.Usuario'),
        ),
        migrations.AddField(
            model_name='medico_informe',
            name='medico_Revision',
            field=models.ForeignKey(to='medico.Medico_Revision'),
        ),
        migrations.AlterUniqueTogether(
            name='medico_citas',
            unique_together=set([('paciente', 'medico', 'institucion', 'fecha')]),
        ),
    ]
