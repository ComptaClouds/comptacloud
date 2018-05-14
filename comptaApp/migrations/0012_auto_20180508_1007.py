# Generated by Django 2.0.4 on 2018-05-08 10:07

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0011_auto_20180507_1251'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
