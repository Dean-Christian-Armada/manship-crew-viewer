# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_auto_20150720_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='present_company',
            field=models.ForeignKey(default=None, verbose_name=b'Present Company', to='website.Company'),
        ),
    ]
