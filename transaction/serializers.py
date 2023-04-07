from _decimal import Decimal
from rest_framework import serializers

from transaction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "id",
            "sender",
            "receiver",
            "transfer_amount",
            "commission",
            "status",
            "timestamp",
        )

    def validate(self, data):
        """
        Validation for check that the sender and receiver
        wallets have the same currency.
        Transactions are available only for wallets with the same currency
        """

        sender_currency = data["sender"].currency
        receiver_currency = data["receiver"].currency
        if sender_currency != receiver_currency:
            raise serializers.ValidationError(
                "Sender and receiver wallets must have the same currency."
            )
        return data

    # def validate_transfer_amount(self, validated_data):
    #     """
    #     Checks the user's balance.
    #     Returns an error if there are not enough funds
    #     """
    #
    #     sender_wallet = self.get_sender_wallet(validated_data)
    #     sender_wallet.is_valid()
    #     if not sender_wallet.filter(
    #         balance__gte=Decimal(
    #             self.context["request"].data["transfer_amount"]
    #         )
    #     ).exists():
    #         raise serializers.ValidationError("Not enough balance")

    def create(self, validated_data):
        """
        Calculate the commission based on whether
        the sender and receiver wallets belong to the same user.
        When user sends money from his wallet to his
        another wallet - no commission, and when he sends
        to wallet, related to another user - commission=10%
        """

        transfer_amount = validated_data["transfer_amount"]
        sender = self.validated_data["sender"]
        receiver = self.validated_data["receiver"]

        if sender.user == receiver.user:
            commission = 0
        else:
            commission = transfer_amount * Decimal("0.1")

        if sender.balance < transfer_amount + commission:
            raise ValueError("Insufficient balance.")

        sender.balance -= transfer_amount + commission
        sender.save()
        receiver.balance += transfer_amount
        receiver.save()

        validated_data["commission"] = commission

        return Transaction.objects.create(**validated_data)
