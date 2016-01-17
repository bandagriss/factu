# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factu', '0003_auto_20151220_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='ci',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='matricula',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
