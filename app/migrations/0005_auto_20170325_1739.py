# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_event_image_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.CharField(max_length=100, default='24 мая 2015'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.CharField(max_length=100, default='Лондон'),
            preserve_default=False,
        ),
    ]
