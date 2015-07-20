# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20150720_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='publications',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
