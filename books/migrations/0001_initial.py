# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=50)),
                ('review', models.TextField(blank=True, null=True)),
                ('date_review', models.DateField(blank=True, null=True)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
