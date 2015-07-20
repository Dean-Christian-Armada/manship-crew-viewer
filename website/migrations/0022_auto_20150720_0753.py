# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_auto_20150720_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='contact_number',
            field=models.IntegerField(max_length=15),
        ),
    ]
