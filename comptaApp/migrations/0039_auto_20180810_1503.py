# Generated by Django 2.0.4 on 2018-08-10 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0038_auto_20180808_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertaxe',
            name='taxeids',
        ),
        migrations.AddField(
            model_name='usertaxe',
            name='taxe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.impotstaxe'),
        ),
    ]
