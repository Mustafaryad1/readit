# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_auto_20180317_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reviewed_by',
            field=models.ForeignKey(blank=True, null=True, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
