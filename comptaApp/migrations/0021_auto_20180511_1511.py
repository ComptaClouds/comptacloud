# Generated by Django 2.0.4 on 2018-05-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0020_auto_20180511_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='entreprise',
            field=models.CharField(default='merde', max_length=255),
        ),
    ]
