# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_remove_application_gross_tonnage'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='gross_tonnage',
            field=models.IntegerField(default=None),
        ),
    ]
