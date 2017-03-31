# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170325_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default='This is cool', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='hashtag',
            field=models.CharField(default='music', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='image_link',
            field=models.CharField(default='https://pp.userapi.com/c626925/v626925096/1a33f/JD7FoQDRqXY.jpg', max_length=1000),
        ),
    ]
