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

    def create(self, validated_data):
        """
        1)  Check how many wallets the user has.
            If the user has 5 or more wallets, then raise Exception

        2)  Add default bonus from bank for each new created wallet:
            if wallet currency USD or EUR - balance=3.00,
            if RUB - balance=100.00
        """

        print(validated_data)
        if Wallet.objects.filter(user__exact=validated_data.get("user")).count() >= 5:
            raise Exception("User can't create more than 5 wallets")
        if validated_data["currency"] in ["USD", "EUR"]:
            validated_data["balance"] += 3
        elif validated_data["currency"] == "RUB":
            validated_data["balance"] += 100

        return Wallet.objects.create(**validated_data)
