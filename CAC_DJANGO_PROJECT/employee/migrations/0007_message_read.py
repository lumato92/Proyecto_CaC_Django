# Generated by Django 3.2.14 on 2022-11-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
