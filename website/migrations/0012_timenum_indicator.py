# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20150720_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='timenum',
            name='indicator',
            field=models.ManyToManyField(to='website.TimeIndicator'),
        ),
    ]
