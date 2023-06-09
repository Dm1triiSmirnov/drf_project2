# Generated by Django 4.2 on 2023-04-06 08:51

from django.db import migrations, models

import wallet.models


class Migration(migrations.Migration):
    dependencies = [
        ("wallet", "0003_alter_wallet_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wallet",
            name="name",
            field=models.CharField(
                default=wallet.models.Wallet.generate_wallet_name,
                editable=False,
                max_length=8,
                unique=True,
            ),
        ),
    ]
