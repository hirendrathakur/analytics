# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0063_auto_20150614_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='dept',
            fields=[
                ('dept_code', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('dept_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='prof_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 22, 59, 32, 871000)),
        ),
        migrations.AlterField(
            model_name='professor',
            name='prof_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 22, 59, 32, 870000)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 22, 59, 32, 873000)),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 22, 59, 32, 865000)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 22, 59, 32, 868000)),
        ),
    ]
