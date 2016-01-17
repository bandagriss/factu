# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_devolucion', models.DateField(auto_now_add=True)),
                ('nota', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=10)),
                ('titulo', models.CharField(max_length=50)),
                ('ejemplares', models.IntegerField()),
                ('fecha_publicacion', models.DateField()),
                ('notas', models.TextField(blank=True)),
                ('area', models.ForeignKey(to='factu.Area')),
                ('autor', models.ManyToManyField(to='factu.Autor')),
                ('editor', models.ForeignKey(to='factu.Editor')),
                ('estado', models.ForeignKey(to='factu.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_prestamo', models.DateField(auto_now_add=True)),
                ('estado', models.CharField(max_length=20)),
                ('fecha_maxDevolucion', models.DateTimeField()),
                ('nota', models.TextField(blank=True)),
                ('libro', models.ForeignKey(to='factu.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.CharField(unique=True, max_length=30)),
                ('contrasenia', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('matricula', models.PositiveIntegerField(unique=True)),
                ('telefono', models.IntegerField(null=True)),
                ('ci', models.PositiveIntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('tipo_usuario', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='prestamo',
            name='usuario',
            field=models.ForeignKey(to='factu.Usuario'),
        ),
        migrations.AddField(
            model_name='libro',
            name='tipo_documento',
            field=models.ForeignKey(to='factu.TipoDocumento'),
        ),
        migrations.AddField(
            model_name='devolucion',
            name='prestamo',
            field=models.ForeignKey(to='factu.Prestamo'),
        ),
    ]
