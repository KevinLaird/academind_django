# Generated by Django 3.2.4 on 2021-07-09 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_auto_20210708_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
