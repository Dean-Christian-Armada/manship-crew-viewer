# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20150720_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company',
            field=models.CharField(max_length=50, unique=True, null=True),
        ),
    ]
