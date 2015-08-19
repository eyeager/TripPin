# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_auto_20150817_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='pins',
            name='state',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
