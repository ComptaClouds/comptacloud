# Generated by Django 2.0.4 on 2018-06-20 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0031_customuser_saisieoccupe'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationcompta',
            name='controleimputation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='operationcompta',
            name='controlesaisie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='operationcompta',
            name='documentid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='comptaApp.Document'),
        ),
    ]