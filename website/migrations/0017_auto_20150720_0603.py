# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20150720_0553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(default=b'N/A', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='present_company',
            field=models.ForeignKey(default=None, to='website.Company'),
        ),
    ]
