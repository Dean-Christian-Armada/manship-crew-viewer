# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20150720_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ces',
            field=models.ForeignKey(default=None, to='website.CES'),
        ),
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='principal',
            name='principal',
            field=models.CharField(max_length=10, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='st_at',
            field=models.CharField(max_length=3, unique=True, null=True),
        ),
    ]
