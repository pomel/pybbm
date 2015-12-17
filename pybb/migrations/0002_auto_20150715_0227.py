# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='poll_is_private',
            field=models.BooleanField(default=False, verbose_name='Poll is private'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(default=b'ru-RU', max_length=10, verbose_name='Language', blank=True, choices=[(b'ru', b'Russian'), (b'en', b'English')]),
            preserve_default=True,
        ),
    ]
