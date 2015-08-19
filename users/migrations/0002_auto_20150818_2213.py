# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='integrationsusers',
            old_name='integration_id',
            new_name='integration',
        ),
        migrations.RenameField(
            model_name='integrationsusers',
            old_name='user_id',
            new_name='user',
        ),
    ]
