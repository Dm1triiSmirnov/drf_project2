from rest_framework import serializers

from wallet.models import BANK_BONUS_RUB, BANK_BONUS_USD_EUR, Wallet


class WalletSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    balance = serializers.DecimalField(max_digits=200, decimal_places=2, default=0, read_only=True)

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

    def create(self, validated_data):
        """
        Add default bonus from bank for each new created wallet:
        if wallet currency USD or EUR - balance=3.00,
        if RUB - balance=100.00
        """

        if validated_data["currency"] in ["USD", "EUR"]:
            balance = BANK_BONUS_USD_EUR
        elif validated_data["currency"] == "RUB":
            balance = BANK_BONUS_RUB

        user = self.context["request"].user

        return Wallet.objects.create(**validated_data,
                                     user=user,
                                     balance=balance)
