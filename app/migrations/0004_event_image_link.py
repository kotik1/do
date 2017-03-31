# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_event_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image_link',
            field=models.CharField(max_length=1000, default='https://pp.userapi.com/c626925/v626925096/1a33f/JD7FoQDRqXY.jpg'),
            preserve_default=False,
        ),
    ]
