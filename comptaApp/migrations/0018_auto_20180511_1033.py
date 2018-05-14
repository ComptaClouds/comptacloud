# Generated by Django 2.0.4 on 2018-05-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0017_auto_20180511_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='autorises',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='standards',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='valides',
        ),
        migrations.AddField(
            model_name='customuser',
            name='autorise',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='standard',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='valide',
            field=models.BooleanField(default=False),
        ),
    ]
