# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disposicion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('proveedor', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('telefono', models.IntegerField()),
                ('productos', models.ManyToManyField(through='blog.Disposicion', to='blog.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='disposicion',
            name='producto',
            field=models.ForeignKey(to='blog.Producto'),
        ),
        migrations.AddField(
            model_name='disposicion',
            name='tienda',
            field=models.ForeignKey(to='blog.Tienda'),
        ),
    ]
