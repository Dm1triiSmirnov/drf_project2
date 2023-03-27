from rest_framework import viewsets

from wallet.models import Transaction, Wallet
from wallet.serializers import TransactionSerializer, WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# class WalletAPIView(generics.ListAPIView):
#     queryset = Wallet.objects.all()
#     serializer_class = WalletSerializer
