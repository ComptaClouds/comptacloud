# Generated by Django 2.0.4 on 2018-05-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0012_auto_20180508_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
