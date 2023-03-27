import random
import string

from django.db import models

WALLET_TYPE = [("Visa", "visa"), ("Mastercard", "mastercard")]
CURRENCY = [("USD", "dollar"), ("EUR", "euro"), ("RUB", "ruble")]
STATUS = [("PAID", "paid"), ("FAILED", "failed")]


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)


class Wallet(models.Model):
    def generate_wallet_name():
        """Function which generate wallet name from unique random 8 symbols of latin alphabet and digits."""
        symbols = string.digits + string.ascii_uppercase
        wallet_name = "".join(random.sample(symbols, 8))

        if wallet_name not in Wallet.objects.all():
            return wallet_name
        else:
            return generate_wallet_name()

    name = models.CharField(max_length=8, unique=True, default=generate_wallet_name)
    type = models.CharField(choices=WALLET_TYPE, max_length=100)
    currency = models.CharField(choices=CURRENCY, max_length=3)
    balance = models.DecimalField(max_digits=200, decimal_places=2)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["user"]


# class Transaction(models.Model):
#     sender =  models.CharField(max_length=8)
#     receiver = models.CharField(max_length=8)
#     transfer_amount = models.FloatField()
#     commission = models.FloatField()
#     status = models.CharField(choices=STATUS, max_length=100)
#     timestamp = models.DateTimeField(auto_now_add=True)
