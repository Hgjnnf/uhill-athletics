# Generated by Django 2.2.6 on 2019-10-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingform',
            name='btime_from',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='btime_to',
            field=models.TimeField(),
        ),
    ]
