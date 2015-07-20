# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_auto_20150720_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='contact_number',
            field=models.CharField(default=None, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{7}|[0-9]{11})$', message=b'Telephone and Mobile Numbers are only allowed')]),
        ),
    ]
