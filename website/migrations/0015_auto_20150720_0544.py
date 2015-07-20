# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20150720_0518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timenum',
            name='indicator',
        ),
        migrations.RemoveField(
            model_name='timerank',
            name='indicator',
        ),
        migrations.RemoveField(
            model_name='timerank',
            name='num',
        ),
        migrations.RemoveField(
            model_name='application',
            name='years_in_rank',
        ),
        migrations.AddField(
            model_name='application',
            name='num_years_rank',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='application',
            name='timeindicator',
            field=models.ForeignKey(default=1, to='website.TimeIndicator'),
        ),
        migrations.DeleteModel(
            name='TimeNum',
        ),
        migrations.DeleteModel(
            name='TimeRank',
        ),
    ]
