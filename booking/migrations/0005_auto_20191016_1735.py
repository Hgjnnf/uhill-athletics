# Generated by Django 2.2.6 on 2019-10-16 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20191011_1751'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bookingForm',
            new_name='bookingData',
        ),
        migrations.RenameField(
            model_name='bookingdata',
            old_name='comment',
            new_name='comments',
        ),
    ]
