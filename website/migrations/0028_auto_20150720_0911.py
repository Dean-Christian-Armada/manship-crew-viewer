# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_auto_20150720_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vtype',
            name='vessel_type',
            field=models.CharField(max_length=50, unique=True, null=True),
        ),
    ]
