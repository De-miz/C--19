# Generated by Django 4.1.2 on 2022-10-27 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('C19app', '0004_alter_comments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 27, 22, 35)),
        ),
    ]
