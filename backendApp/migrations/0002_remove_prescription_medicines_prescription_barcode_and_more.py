# Generated by Django 5.0.4 on 2024-05-01 00:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backendApp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prescription",
            name="medicines",
        ),
        migrations.AddField(
            model_name="prescription",
            name="barcode",
            field=models.CharField(
                default=uuid.uuid4, editable=False, max_length=100, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="purchase",
            name="purchase_date",
            field=models.DateField(),
        ),
    ]