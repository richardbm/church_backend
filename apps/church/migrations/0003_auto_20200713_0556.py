# Generated by Django 3.0.3 on 2020-07-13 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0002_auto_20200713_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactparameter',
            name='label',
            field=models.CharField(choices=[('ADDRESS', 'Address'), ('PHONE_NUMBER', 'Phone number'), ('EMAIL', 'Email'), ('MAP', 'Map')], max_length=32),
        ),
    ]
