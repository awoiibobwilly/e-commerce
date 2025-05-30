# Generated by Django 5.2 on 2025-05-06 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fulfilment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("centre_location", models.CharField(max_length=100)),
                ("picking_status", models.CharField(max_length=50)),
                ("packaging_type", models.CharField(max_length=50)),
                ("stock_allocated", models.BooleanField(default=False)),
                ("sla_tracker", models.DurationField()),
                ("internal_notes", models.TextField()),
                ("courier_handoff_status", models.CharField(max_length=50)),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="order.order"
                    ),
                ),
            ],
        ),
    ]
