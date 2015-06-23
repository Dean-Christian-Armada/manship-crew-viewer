# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crew', '0002_cert_groups_component_scales_components_contracts_country_manning_agent_official_signers_tax_categor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CERT_GROUPS',
        ),
        migrations.DeleteModel(
            name='COMPONENT_SCALES',
        ),
        migrations.DeleteModel(
            name='Components',
        ),
        migrations.DeleteModel(
            name='MANNING_AGENT',
        ),
        migrations.DeleteModel(
            name='OFFICIAL_SIGNERS',
        ),
        migrations.DeleteModel(
            name='RequiredCertificates',
        ),
        migrations.DeleteModel(
            name='TAX_CATEGORIES',
        ),
        migrations.DeleteModel(
            name='VESSEL_CATEGORIES',
        ),
        migrations.DeleteModel(
            name='WAGES',
        ),
        migrations.RemoveField(
            model_name='contracts',
            name='CON_MAN_KEY',
        ),
        migrations.RemoveField(
            model_name='contracts',
            name='CON_Wage_W_REC',
        ),
        migrations.RemoveField(
            model_name='ranks',
            name='R_TC_KEY',
        ),
    ]
