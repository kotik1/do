# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date_of_start', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=1000)),
                ('place', models.CharField(max_length=1000)),
                ('date', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('hashtag', models.CharField(max_length=1000)),
                ('image_link', models.CharField(default='https://pp.userapi.com/c626925/v626925096/1a33f/JD7FoQDRqXY.jpg', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=2000)),
                ('dialog', models.ForeignKey(related_name='dialog_reverse', to='app.Dialog')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('upload', models.FileField(upload_to='media/tickets/')),
                ('comment', models.CharField(max_length=2000)),
                ('approved', models.BooleanField(default=False)),
                ('sold', models.BooleanField(default=False)),
                ('price', models.IntegerField(default=0)),
                ('ticket_type', models.CharField(default='Digital', choices=[('DG', 'Digital'), ('RL', 'Real')], max_length=2)),
                ('event', models.ForeignKey(to='app.Event')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('sn_link', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(blank=True)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('sn_id', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='ownership',
            field=models.ForeignKey(to='app.UserProfile'),
        ),
        migrations.AddField(
            model_name='message',
            name='from_user',
            field=models.ForeignKey(related_name='from_user_reverse', to='app.UserProfile'),
        ),
        migrations.AddField(
            model_name='message',
            name='to_user',
            field=models.ForeignKey(related_name='to_user_reverse', to='app.UserProfile'),
        ),
        migrations.AddField(
            model_name='dialog',
            name='buyer',
            field=models.ForeignKey(related_name='buyer_reverse', to='app.UserProfile'),
        ),
        migrations.AddField(
            model_name='dialog',
            name='sales',
            field=models.ForeignKey(related_name='sales_reverse', to='app.UserProfile'),
        ),
        migrations.AddField(
            model_name='dialog',
            name='ticket',
            field=models.ForeignKey(to='app.Ticket'),
        ),
    ]
