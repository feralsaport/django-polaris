# Generated by Django 2.2.18 on 2021-02-05 01:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polaris", "0008_transaction_pending_execution_attempt"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="client_domain",
            field=models.TextField(blank=True, null=True),
        ),
    ]
