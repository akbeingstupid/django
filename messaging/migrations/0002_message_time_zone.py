# Generated by Django 2.1.5 on 2019-05-10 12:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time_zone',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]