# Generated by Django 3.0.3 on 2021-01-17 23:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ministries', '0004_auto_20200727_0307'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('church', '0005_news_expires_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('member_since', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MemberMinistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('member_type', models.CharField(choices=[('DISCIPLE', 'CHURCH_MEMBER_TYPE_DISCIPLE'), ('COLLABORATOR', 'CHURCH_MEMBER_TYPE_COLLABORATOR'), ('LEADER', 'CHURCH_MEMBER_TYPE_LEADER')], max_length=16)),
                ('is_baptized', models.BooleanField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ministries', to='church.Membership')),
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='members', to='ministries.Ministry')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]