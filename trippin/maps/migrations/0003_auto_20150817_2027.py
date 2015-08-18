# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_auto_20150817_0041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkins',
            old_name='pin_id',
            new_name='pin',
        ),
        migrations.RenameField(
            model_name='checkins',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='pins',
            old_name='integration_id',
            new_name='integration',
        ),
    ]
