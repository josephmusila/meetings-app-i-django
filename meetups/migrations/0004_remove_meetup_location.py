# Generated by Django 2.2.18 on 2022-01-09 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_auto_20220109_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetup',
            name='location',
        ),
    ]