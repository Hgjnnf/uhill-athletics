# Generated by Django 2.2.6 on 2019-10-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20191011_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingform',
            name='btime_from',
        ),
        migrations.RemoveField(
            model_name='bookingform',
            name='btime_to',
        ),
        migrations.AddField(
            model_name='bookingform',
            name='book_from',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookingform',
            name='book_until',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookingform',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='first_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='last_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
