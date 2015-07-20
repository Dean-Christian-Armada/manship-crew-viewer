# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0030_auto_20150720_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='gross_tonnage',
        ),
    ]
