# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0037_auto_20150722_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='contact_number',
            field=models.CharField(default=None, validators=[django.core.validators.RegexValidator(regex=b'^([0-9]{7}|[0-9]{11})$', message=b'Telephone and Mobile Numbers are only allowed')], max_length=15, blank=True, null=True, verbose_name=b'Contact Number'),
        ),
        migrations.AlterField(
            model_name='application',
            name='time_indicator',
            field=models.ForeignKey(default=1, verbose_name=b'Time Indicator', to='website.TimeIndicator'),
        ),
        migrations.AlterField(
            model_name='application',
            name='vessel_type',
            field=models.ForeignKey(verbose_name=b'Vessel Type', to='website.VType'),
        ),
    ]
