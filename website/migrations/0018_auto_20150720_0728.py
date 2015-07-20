# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20150720_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company',
            field=models.CharField(max_length=50),
        ),
    ]
