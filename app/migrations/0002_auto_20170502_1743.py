# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='number_of_friends',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture_link',
            field=models.CharField(default='https://pp.userapi.com/c626925/v626925096/1a33f/JD7FoQDRqXY.jpg', max_length=2000),
        ),
        migrations.AlterField(
            model_name='dialog',
            name='date_of_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='comment',
            field=models.CharField(default='I am sick and tired', max_length=2000),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='upload',
            field=models.FileField(upload_to='pdf/', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
