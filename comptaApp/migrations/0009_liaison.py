# Generated by Django 2.0.4 on 2018-05-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0008_fournisseurs'),
    ]

    operations = [
        migrations.CreateModel(
            name='liaison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrepriseid', models.CharField(default='merde', max_length=255)),
                ('comptableid', models.CharField(default='merde', max_length=255)),
            ],
        ),
    ]
