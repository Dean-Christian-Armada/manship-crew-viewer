# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20150720_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timenum',
            name='num',
            field=models.FloatField(),
        ),
    ]
