# Generated by Django 2.2.16 on 2020-11-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polaris", "0003_auto_20201009_1300"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="claimable_balance_id",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="transaction",
            name="claimable_balance_supported",
            field=models.BooleanField(default=False),
        ),
    ]
