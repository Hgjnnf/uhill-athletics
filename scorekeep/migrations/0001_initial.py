# Generated by Django 2.2.6 on 2019-12-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreCreate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('home', models.CharField(max_length=120)),
                ('away', models.CharField(max_length=1200)),
                ('date', models.DateField()),
                ('startTime', models.TimeField()),
            ],
        ),
    ]
