# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_ticket_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='price',
        ),
    ]
