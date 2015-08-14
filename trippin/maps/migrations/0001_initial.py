# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_check_in_id', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pins',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_venue_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('longitude', models.DecimalField(max_digits=15, decimal_places=14)),
                ('latitude', models.DecimalField(max_digits=15, decimal_places=14)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
                ('integration_id', models.ForeignKey(to='users.Integrations')),
            ],
        ),
        migrations.AddField(
            model_name='checkins',
            name='pin_id',
            field=models.ForeignKey(to='maps.Pins'),
        ),
        migrations.AddField(
            model_name='checkins',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
