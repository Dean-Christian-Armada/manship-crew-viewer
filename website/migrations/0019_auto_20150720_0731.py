# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20150720_0728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=10, unique=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='company',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AddField(
            model_name='application',
            name='position_applied',
            field=models.ForeignKey(default=None, to='website.Position'),
        ),
    ]
