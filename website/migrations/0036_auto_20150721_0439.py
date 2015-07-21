# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0035_auto_20150721_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ces',
            field=models.ForeignKey(default=None, verbose_name=b'CES', to='website.CES'),
        ),
    ]
