from django.db import models

STATUS = [("PAID", "paid"), ("FAILED", "failed")]


class Transaction(models.Model):
    sender = models.ForeignKey(
        "wallet.Wallet",
        on_delete=models.CASCADE,
        related_name="sender",
        to_field="name",  # noqa E501
    )
    receiver = models.ForeignKey(
        "wallet.Wallet",
        on_delete=models.CASCADE,
        related_name="receiver",
        to_field="name",  # noqa E501
    )
    transfer_amount = models.FloatField()
    commission = models.FloatField()
    status = models.CharField(choices=STATUS, max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
