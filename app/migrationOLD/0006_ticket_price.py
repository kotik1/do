# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_ticket_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='price',
            field=models.IntegerField(blank=True, default=100),
            preserve_default=False,
        ),
    ]
