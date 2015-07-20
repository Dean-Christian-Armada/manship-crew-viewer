# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20150720_0544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='timeindicator',
            new_name='time_indicator',
        ),
        migrations.AlterField(
            model_name='application',
            name='interview_1',
            field=models.CharField(default=None, max_length=2, choices=[(b'-', b'-'), (b'N/A', b'N/A'), (b'A', b'A'), (b'P', b'P'), (b'X', b'X')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='interview_2',
            field=models.CharField(default=None, max_length=2, choices=[(b'-', b'-'), (b'N/A', b'N/A'), (b'A', b'A'), (b'P', b'P'), (b'X', b'X')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='interview_3',
            field=models.CharField(default=None, max_length=2, choices=[(b'-', b'-'), (b'N/A', b'N/A'), (b'A', b'A'), (b'P', b'P'), (b'X', b'X')]),
        ),
    ]
