# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20150720_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usvisa',
            name='visa',
            field=models.CharField(default=b'NONE', max_length=6, unique=True, null=True),
        ),
    ]
