# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_auto_20170328_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('sold', models.BooleanField(default=False)),
                ('event', models.OneToOneField(to='app.Event')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('sn_link', models.CharField(max_length=100)),
                ('sn', models.CharField(choices=[('1', 'facebook'), ('2', 'vk')], max_length=2)),
                ('phone_number', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userpofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserPofile',
        ),
        migrations.AddField(
            model_name='ticket',
            name='ownership',
            field=models.OneToOneField(to='app.UserProfile'),
        ),
    ]
