# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_dialog_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='dialog',
            name='text',
            field=models.CharField(default='ggg', max_length=2000),
            preserve_default=False,
        ),
    ]
