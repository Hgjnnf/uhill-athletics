# Generated by Django 2.2.6 on 2019-11-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20191024_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdata',
            name='book_from',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='bookingdata',
            name='book_until',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='bookingdata',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='bookingdata',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='bookingdata',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='bookingdata',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
