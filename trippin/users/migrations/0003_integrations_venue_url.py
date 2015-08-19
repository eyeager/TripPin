# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150818_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrations',
            name='venue_url',
            field=models.CharField(default='http://foursquare.com/v/', max_length=128),
            preserve_default=False,
        ),
    ]
