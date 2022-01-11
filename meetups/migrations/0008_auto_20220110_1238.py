# Generated by Django 2.2.18 on 2022-01-10 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0007_auto_20220110_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2022-01-02'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='rest@test.com', max_length=254),
            preserve_default=False,
        ),
    ]
