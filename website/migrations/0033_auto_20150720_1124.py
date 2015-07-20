# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0032_application_gross_tonnage'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='Dean_Armada',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='IsActive',
            field=models.BooleanField(default=True, verbose_name=b'Present Company'),
        ),
        migrations.AlterField(
            model_name='application',
            name='application_date',
            field=models.ForeignKey(verbose_name=b'Application Date', to='website.Date'),
        ),
        migrations.AlterField(
            model_name='application',
            name='date_modified',
            field=models.DateTimeField(null=True, editable=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='gross_tonnage',
            field=models.IntegerField(default=None, verbose_name=b'Gross Tonnage'),
        ),
        migrations.AlterField(
            model_name='application',
            name='us_visa',
            field=models.ForeignKey(verbose_name=b'US Visa', to='website.USVisa'),
        ),
    ]
