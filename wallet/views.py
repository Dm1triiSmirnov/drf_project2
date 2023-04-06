from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from wallet.models import Wallet
from wallet.serializers import WalletSerializer


class WalletsListCreateViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def list(self, request, *args, **kwargs) -> Response:
        """Get all wallets for current user"""

        queryset = Wallet.objects.filter(user=request.user)
        serializer = WalletSerializer(queryset, many=True)
        if queryset:
            return Response(serializer.data)
        return Response("No wallets for current user", status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs) -> Response:
        """Create new wallet"""

        serializer = WalletSerializer(data=request.data, context={"request": request})
        return Response(serializer.data)


class WalletsRetrieveDestroyViewSet(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    lookup_field = "name"
