from django.db.models import Q
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response

from wallet.models import MAX_WALLETS, Wallet
from wallet.serializers import WalletSerializer


class WalletsListCreateViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs) -> Response:
        """Get all wallets for current user"""

        queryset = Wallet.objects.filter(user=request.user)
        serializer = WalletSerializer(queryset, many=True)
        if queryset:
            return Response(serializer.data)
        return Response("No wallets for current user", status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs) -> Response:
        """Create new wallet.
        Check how many wallets the user has.
        If the user has 5 or more wallets, then raise Exception
        """

        serializer = WalletSerializer(data=request.data, context={"request": request})
        count_wallets = Wallet.objects.filter(user=request.user).count()

        if count_wallets >= MAX_WALLETS:
            return Response(
                {"max_wallets": MAX_WALLETS}, status=status.HTTP_400_BAD_REQUEST
            )
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WalletsRetrieveDestroyViewSet(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    lookup_field = "name"
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs) -> Response:
        """
        Delete wallet.
        Performs check if the user is not the owner of the wallet,
        then returns an error.
        """

        queryset = Wallet.objects.filter(
            Q(user=request.user) & Q(name=self.kwargs.get("name"))
        )

        if not queryset:
            return Response(
                "User can delete only own wallets", status=status.HTTP_403_FORBIDDEN
            )

        wallet = self.get_object()
        wallet.delete()

        return Response({"Message": "Wallet has been deleted"})

    def retrieve(self, request, *args, **kwargs) -> Response:
        """Retrieve wallet details.
        Perform check if user is not owner of the wallet,
        then return error.
        """

        queryset = Wallet.objects.filter(
            Q(user=request.user) & Q(name=self.kwargs.get("name"))
        )

        if not queryset:
            return Response(
                "User can view only own wallets", status=status.HTTP_403_FORBIDDEN
            )

        serializer = WalletSerializer(queryset, many=True)

        return Response(serializer.data)
