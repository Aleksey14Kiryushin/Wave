# Generated by Django 4.0.6 on 2022-07-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default='21:53'),
        ),
    ]
