# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150716_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('gross_tonnage', models.IntegerField()),
                ('contact_number', models.IntegerField()),
                ('remarks', models.TextField()),
                ('interview_1', models.CharField(default=b'', max_length=2, choices=[(b'', b''), (b'A', b'A'), (b'H', b'H'), (b'X', b'X')])),
                ('interview_2', models.CharField(default=b'', max_length=2, choices=[(b'', b''), (b'A', b'A'), (b'H', b'H'), (b'X', b'X')])),
                ('interview_3', models.CharField(default=b'', max_length=2, choices=[(b'', b''), (b'A', b'A'), (b'H', b'H'), (b'X', b'X')])),
                ('age', models.ForeignKey(to='website.Age')),
                ('application_source', models.ForeignKey(to='website.AppSource')),
                ('availability', models.ForeignKey(to='website.Availability')),
                ('date', models.ForeignKey(to='website.Date')),
                ('principal', models.ForeignKey(to='website.Principal')),
                ('st_at', models.ForeignKey(to='website.StAt')),
                ('us_visa', models.ForeignKey(to='website.USVisa')),
                ('vessel_type', models.ForeignKey(to='website.VType')),
                ('years_in_rank', models.ForeignKey(to='website.TimeRank')),
            ],
        ),
        migrations.RemoveField(
            model_name='applications',
            name='age',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='application_source',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='date',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='principal',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='st_at',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='us_visa',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='vessel_type',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='years_in_rank',
        ),
        migrations.DeleteModel(
            name='Applications',
        ),
    ]
