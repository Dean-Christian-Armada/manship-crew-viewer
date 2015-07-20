# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='interview_2',
            field=models.CharField(default=b'', max_length=2, choices=[(b'', b''), (b'A', b'A'), (b'H', b'H'), (b'X', b'X')]),
        ),
        migrations.AddField(
            model_name='applications',
            name='interview_3',
            field=models.CharField(default=b'', max_length=2, choices=[(b'', b''), (b'A', b'A'), (b'H', b'H'), (b'X', b'X')]),
        ),
        migrations.AlterField(
            model_name='applications',
            name='interview_1',
            field=models.CharField(default=b'', max_length=2, choices=[(b'', b''), (b'A', b'A'), (b'H', b'H'), (b'X', b'X')]),
        ),
        migrations.DeleteModel(
            name='InterviewVal',
        ),
    ]
