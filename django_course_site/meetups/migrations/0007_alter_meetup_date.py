# Generated by Django 3.2.4 on 2021-07-09 04:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0006_alter_meetup_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]