# Generated by Django 2.2.6 on 2019-10-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20191016_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdata',
            name='room',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]