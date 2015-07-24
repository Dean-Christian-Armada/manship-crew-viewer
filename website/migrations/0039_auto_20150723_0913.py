# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0038_auto_20150722_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='num_years_rank',
            field=models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
