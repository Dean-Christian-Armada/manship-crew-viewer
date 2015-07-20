# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20150716_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='ces',
            field=models.ForeignKey(default=1, to='website.CES'),
        ),
        migrations.AlterField(
            model_name='application',
            name='interview_1',
            field=models.CharField(default=b'', max_length=2, choices=[(b'-', b'-'), (b'N/A', b'N/A'), (b'A', b'A'), (b'P', b'P'), (b'X', b'X')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='interview_2',
            field=models.CharField(default=b'', max_length=2, choices=[(b'-', b'-'), (b'N/A', b'N/A'), (b'A', b'A'), (b'P', b'P'), (b'X', b'X')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='interview_3',
            field=models.CharField(default=b'', max_length=2, choices=[(b'-', b'-'), (b'N/A', b'N/A'), (b'A', b'A'), (b'P', b'P'), (b'X', b'X')]),
        ),
    ]
