# Generated by Django 4.1.2 on 2022-10-27 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('C19app', '0009_comments_date_alter_comments_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='time',
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
