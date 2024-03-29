# Generated by Django 3.2.4 on 2021-07-09 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0007_alter_meetup_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='meetup',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetups.organizer'),
        ),
    ]
