# Generated by Django 4.0.6 on 2022-07-07 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 7, 16, 56, 16, 334385)),
        ),
    ]
