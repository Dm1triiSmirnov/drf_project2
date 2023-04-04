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
    transfer_amount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )  # noqa E501
    commission = models.DecimalField(
        max_digits=12, decimal_places=2, default=0, editable=False
    )
    status = models.CharField(
        choices=STATUS, max_length=100, default="PAID", editable=False
    )
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
