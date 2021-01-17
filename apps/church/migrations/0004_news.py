# Generated by Django 3.0.3 on 2021-01-17 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0003_auto_20200713_0556'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=140)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
