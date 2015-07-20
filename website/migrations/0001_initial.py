# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('gross_tonnage', models.IntegerField()),
                ('contact_number', models.IntegerField()),
                ('remarks', models.TextField()),
                ('age', models.ForeignKey(to='website.Age')),
            ],
        ),
        migrations.CreateModel(
            name='AppSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=30, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('availability', models.CharField(default=b'Anytime', unique=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CES',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ces', models.CharField(max_length=3, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewVal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('val', models.CharField(unique=True, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('principal', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StAt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('st_at', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeIndicator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indicator', models.CharField(default=b'Years', unique=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TimeNum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeRank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indicator', models.ForeignKey(to='website.TimeIndicator')),
                ('num', models.ForeignKey(to='website.TimeNum')),
            ],
        ),
        migrations.CreateModel(
            name='USVisa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visa', models.CharField(default=b'NONE', max_length=5, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vessel_type', models.CharField(max_length=20, unique=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='applications',
            name='application_source',
            field=models.ForeignKey(to='website.AppSource'),
        ),
        migrations.AddField(
            model_name='applications',
            name='availability',
            field=models.ForeignKey(to='website.Availability'),
        ),
        migrations.AddField(
            model_name='applications',
            name='date',
            field=models.ForeignKey(to='website.Date'),
        ),
        migrations.AddField(
            model_name='applications',
            name='interview_1',
            field=models.ForeignKey(to='website.InterviewVal'),
        ),
        migrations.AddField(
            model_name='applications',
            name='principal',
            field=models.ForeignKey(to='website.Principal'),
        ),
        migrations.AddField(
            model_name='applications',
            name='st_at',
            field=models.ForeignKey(to='website.StAt'),
        ),
        migrations.AddField(
            model_name='applications',
            name='us_visa',
            field=models.ForeignKey(to='website.USVisa'),
        ),
        migrations.AddField(
            model_name='applications',
            name='vessel_type',
            field=models.ForeignKey(to='website.VType'),
        ),
        migrations.AddField(
            model_name='applications',
            name='years_in_rank',
            field=models.ForeignKey(to='website.TimeRank'),
        ),
    ]
