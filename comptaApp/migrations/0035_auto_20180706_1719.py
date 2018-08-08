from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0034_auto_20180706_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='imputation',
            fields=[
                ('imputationid', models.AutoField(primary_key=True, serialize=False)),
                ('misajour', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('operation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='comptaApp.operationcompta')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='credit',
            name='imputation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.imputation'),
        ),
        migrations.AddField(
            model_name='debit',
            name='imputation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.imputation'),
        ),
    ]