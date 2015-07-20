# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_auto_20150720_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='remarks',
            field=models.TextField(null=True, blank=True),
        ),
    ]
