# Generated by Django 2.0.4 on 2018-04-23 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0002_customuser_secondname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': (('can_see_dealer_price', 'Can see dealer price'),)},
        ),
    ]
