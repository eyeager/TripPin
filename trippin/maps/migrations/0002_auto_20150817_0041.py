# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pins',
            name='latitude',
            field=models.DecimalField(max_digits=20, decimal_places=14),
        ),
        migrations.AlterField(
            model_name='pins',
            name='longitude',
            field=models.DecimalField(max_digits=20, decimal_places=14),
        ),
    ]
