# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factu', '0002_auto_20151220_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='ci',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='matricula',
            field=models.IntegerField(unique=True),
        ),
    ]
