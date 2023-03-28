from rest_framework import viewsets

from wallet.models import Wallet
from wallet.serializers import WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
