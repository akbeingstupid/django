# Generated by Django 2.1.5 on 2019-05-10 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_message_time_zone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='time_zone',
            new_name='timestamp',
        ),
    ]
