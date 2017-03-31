# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170330_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='upload',
            field=models.FileField(upload_to='/tickets/', default='https://pp.userapi.com/c626925/v626925096/1a33f/JD7FoQDRqXY.jpg'),
        ),
    ]
