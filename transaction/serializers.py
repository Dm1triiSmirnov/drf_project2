from _decimal import Decimal
from django.db.models import F
from rest_framework import serializers

from transaction.models import Transaction
from wallet.models import Wallet


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

    def check_wallet_exists(self, wallet_name):
        """Check that the <wallet_name> exist"""
        return Wallet.objects.filter(name=wallet_name).exists()

    def check_sender_is_owner(self, sender):
        """Check that sender is the owner of the wallet"""
        user_id = self.context["request"].user.id
        sender_id = sender.user.id
        if sender_id != user_id:
            raise serializers.ValidationError("You don't own this wallet.")

    def validate_sender_balance(self, validated_data, commission):
        """
        Checks the user's balance.
        Returns an error if there are not enough funds
        """
        sender_wallet = Wallet.objects.filter(
            name=self.validated_data["sender"]
        )
        if not sender_wallet.filter(
            balance__gte=Decimal(
                self.context["request"].data["transfer_amount"]
            ) + commission
        ).exists():
            raise serializers.ValidationError("Insufficient balance")

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

        if not self.check_wallet_exists(sender):
            raise serializers.ValidationError(
                f"Wallet {sender} does not exist"
            )

        if not self.check_wallet_exists(receiver):
            raise serializers.ValidationError(
                f"Wallet {receiver} does not exist"
            )

        self.check_sender_is_owner(sender)

        if sender.user == receiver.user:
            commission = 0
        else:
            commission = transfer_amount * Decimal("0.1")

        self.validate_sender_balance(validated_data, commission)

        sender.balance = F("balance") - (transfer_amount + commission)
        sender.save()
        receiver.balance = F("balance") + transfer_amount
        receiver.save()

        validated_data["commission"] = commission

        return Transaction.objects.create(**validated_data)
