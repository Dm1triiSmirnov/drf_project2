from rest_framework import serializers

from wallet.models import Transaction, Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = (
            "id",
            "user",
            "name",
            "type",
            "currency",
            "balance",
            "created_on",
            "modified_on",
        )


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
