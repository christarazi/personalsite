# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fortune',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('filename', models.CharField(max_length=200)),
                ('size', models.IntegerField()),
                ('aphorism', models.CharField(max_length=2150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
