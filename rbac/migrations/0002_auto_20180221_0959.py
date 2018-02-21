# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-21 09:59
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rbacuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='rbacuser',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='rbacpermission',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rbacpermission',
            name='touch_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='rbacpermissionprofile',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rbacpermissionprofile',
            name='touch_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='rbacrole',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rbacrole',
            name='touch_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='rbacroleprofile',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rbacroleprofile',
            name='touch_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='rbacsession',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rbacsession',
            name='touch_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='rbacssdset',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rbacssdset',
            name='touch_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='rbacuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='rbacuserassignment',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rbacuserassignment',
            name='touch_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]