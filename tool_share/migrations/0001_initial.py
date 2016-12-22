# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-07 19:50
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import tool_share.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_auto_20161204_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name='last name')),
                ('picture_path', models.FileField(blank=True, null=True, upload_to=tool_share.models.concatMediaPathUser)),
                ('zip_code', models.IntegerField(validators=[django.core.validators.RegexValidator(message='Zip Code is invalid.', regex='^[0-9]{5}(?:-[0-9]{4})?$')], verbose_name='zip code')),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='phone number')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='address')),
                ('is_coordinator', models.BooleanField(default=False)),
                ('preferences', models.IntegerField(choices=[(0, 'Member, Tool, Admin Join/Leave Shed'), (1, 'Reservation Reminder')], default=0)),
                ('last_notification_visit', models.DateTimeField(default=datetime.datetime(2016, 12, 7, 14, 50, 20, 298104))),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('type', models.IntegerField(choices=[(0, 'Coordinator Joined Shed'), (1, 'Coordinator Left Shed'), (2, 'Member Joined Shed'), (3, 'Member Left Shed'), (4, 'Shed Street Address Changed'), (5, 'Reservation Reminder'), (6, 'Lender Needs to Verify Tool'), (7, 'Lender Needs to Approve Request'), (8, 'Request Approved'), (11, 'Request Declined'), (9, 'Cancellation by Borrower'), (10, 'Cancellation by Lender')], default=-1, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('borrower', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='other_user', to=settings.AUTH_USER_MODEL)),
                ('display_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='display_to', to=settings.AUTH_USER_MODEL)),
                ('lender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resv_type', models.IntegerField(choices=[(0, 'Owner Blocked Out'), (1, "Awaiting Borrower's Approval"), (2, 'Lender Approved'), (3, 'Lender Rejected'), (4, 'Cancelled by Lender'), (5, 'Cancelled by Borrower'), (6, 'Unblocked by Owner')], default=1)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('message_from_borrower', models.TextField(blank=True, max_length=255, null=True)),
                ('reason_for_rejection', models.TextField(blank=True, max_length=255, null=True)),
                ('borrower', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShareZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sheds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.IntegerField(unique=True)),
                ('street_address', models.CharField(max_length=55)),
                ('city', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ToolItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_path', models.FileField(blank=True, null=True, upload_to=tool_share.models.concatMediaPath)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('special_instructions', models.TextField(blank=True, max_length=255)),
                ('pickupDropLoc', models.IntegerField(choices=[(0, 'Shed'), (1, 'Home')], default=0)),
                ('activation', models.IntegerField(choices=[(0, 'Deactivated'), (1, 'Activated')], default=1)),
                ('condition', models.IntegerField(choices=[(0, 'Good'), (1, 'Poor'), (2, 'Broken'), (3, 'Missing')], default=0)),
                ('possession', models.IntegerField(choices=[(0, 'Picked up'), (1, 'Returned'), (2, 'Verified')], default=2)),
                ('ownedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='tool',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tool_share.ToolItem'),
        ),
        migrations.AddField(
            model_name='notification',
            name='tool',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tool_share.ToolItem'),
        ),
    ]
