# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_auto_20150721_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='gross_tonnage',
            field=models.IntegerField(default=None, verbose_name=b'Gross Tonnage'),
        ),
    ]
