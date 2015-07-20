# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0033_auto_20150720_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='Dean_Armada',
        ),
        migrations.AlterField(
            model_name='application',
            name='IsActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='application_source',
            field=models.ForeignKey(verbose_name=b'Application Source', to='website.AppSource'),
        ),
        migrations.AlterField(
            model_name='application',
            name='gross_tonnage',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='application',
            name='position_applied',
            field=models.ForeignKey(default=None, verbose_name=b'Position Applied', to='website.Position'),
        ),
        migrations.AlterField(
            model_name='application',
            name='present_company',
            field=models.ForeignKey(default=None, verbose_name=b'Preset Company', to='website.Company'),
        ),
    ]
