import random
import string

from django.db import models

WALLET_TYPE = [("Visa", "visa"), ("Mastercard", "mastercard")]
CURRENCY = [("USD", "dollar"), ("EUR", "euro"), ("RUB", "ruble")]
MAX_WALLETS = 5
BANK_BONUS_USD_EUR = 3
BANK_BONUS_RUB = 100


class Wallet(models.Model):
    def generate_wallet_name() -> str:
        """Function which generate wallet name from unique
        random 8 symbols of latin alphabet and digits."""

        symbols = string.digits + string.ascii_uppercase
        wallet_name = "".join(random.sample(symbols, 8))

        if wallet_name not in Wallet.objects.all():
            return wallet_name
        else:
            return generate_wallet_name()  # noqa F821

    name = models.CharField(
        max_length=8, unique=True, default=generate_wallet_name, editable=False
    )
    type = models.CharField(choices=WALLET_TYPE, max_length=100, default="Visa")
    currency = models.CharField(max_length=3, choices=CURRENCY, default="EUR")
    balance = models.DecimalField(max_digits=200, decimal_places=2)
    user = models.ForeignKey(
        "auth.User", related_name="owner", on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["user"]

    def __str__(self):
        return self.name
