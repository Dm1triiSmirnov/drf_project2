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
