# Generated by Django 3.0.3 on 2020-07-27 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0012_auto_20191025_1852'),
        ('ministries', '0002_auto_20200720_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='ministry',
            name='events',
            field=models.ManyToManyField(related_name='ministries', to='schedule.Event'),
        ),
    ]
