# Generated by Django 2.2.3 on 2019-07-31 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20190731_1048'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile'),
        ),
    ]
