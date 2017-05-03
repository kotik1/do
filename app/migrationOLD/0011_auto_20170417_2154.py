# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_event_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_type',
        ),
    ]
