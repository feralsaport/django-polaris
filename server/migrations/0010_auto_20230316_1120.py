# Generated by Django 3.2.18 on 2023-03-16 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0009_auto_20211028_2139"),
    ]

    operations = [
        migrations.AddField(
            model_name="polarisuser",
            name="photo_id_back_provided",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="polarisuser",
            name="photo_id_front_provided",
            field=models.BooleanField(default=False),
        ),
    ]
