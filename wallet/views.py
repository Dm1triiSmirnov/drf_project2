from rest_framework import mixins, viewsets

from wallet.models import Wallet
from wallet.serializers import WalletSerializer


class WalletsListCreateViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               viewsets.GenericViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletsRetrieveDestroyViewSet(mixins.RetrieveModelMixin,
                                    mixins.DestroyModelMixin,
                                    viewsets.GenericViewSet,):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    lookup_field = "name"
