# Generated by Django 4.1.7 on 2023-03-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wallet", "0002_remove_user_created_on"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                ("sender", models.CharField(max_length=8)),
                ("receiver", models.CharField(max_length=8)),
                ("transfer_amount", models.FloatField()),
                ("commission", models.FloatField()),
                (
                    "status",
                    models.CharField(
                        choices=[("PAID", "paid"), ("FAILED", "failed")],
                        max_length=100,  # noqa E501
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
