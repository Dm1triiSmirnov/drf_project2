from rest_framework import serializers

from wallet.models import Wallet


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
