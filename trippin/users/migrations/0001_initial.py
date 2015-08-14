# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Integrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('client_key', models.CharField(max_length=128)),
                ('client_secret', models.CharField(max_length=128)),
                ('setup_url', models.CharField(max_length=384)),
                ('data_url', models.CharField(max_length=384)),
            ],
        ),
        migrations.CreateModel(
            name='IntegrationsUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth_key', models.CharField(max_length=128)),
                ('is_active', models.BooleanField()),
                ('integration_id', models.ForeignKey(to='users.Integrations')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
