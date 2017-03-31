# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170328_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_link',
            field=models.CharField(max_length=2000, default='https://pp.userapi.com/c626925/v626925096/1a33f/JD7FoQDRqXY.jpg'),
        ),
    ]
