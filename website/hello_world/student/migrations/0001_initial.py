# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enrollment_number', models.CharField(unique=True, max_length=15)),
                ('name', models.TextField()),
                ('course', models.CharField(max_length=20)),
                ('dob', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
