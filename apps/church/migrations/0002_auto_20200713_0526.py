# Generated by Django 3.0.3 on 2020-07-13 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactparameter',
            options={'ordering': ('label',)},
        ),
    ]
