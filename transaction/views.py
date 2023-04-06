from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.db.models import Q

from transaction.models import Transaction
from transaction.serializers import TransactionSerializer


class TransactionListCreateViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def list(self, request, *args, **kwargs) -> Response:
        """Get all transactions for current user"""

        queryset = Transaction.objects.filter(
            Q(sender__user=request.user) | Q(receiver__user=request.user)
        )
        serializer = TransactionSerializer(queryset, many=True)
        if queryset:
            return Response(serializer.data)
        return Response("No transactions for current user",
                        status=status.HTTP_404_NOT_FOUND)


class TransactionRetrieveDestroyViewSet(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionListAPIView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request, *args, **kwargs) -> Response:
        """Get all transactions where <wallet_name> was sender or receiver"""

        queryset = Transaction.objects.filter(
            (
                    Q(sender__name=self.kwargs.get("pk"))
                    | Q(receiver__name=self.kwargs.get("pk"))
            )
            & (Q(sender__user=request.user) | Q(receiver__user=request.user))
        )

        serializer = TransactionSerializer(queryset, many=True)
        if queryset:
            return Response(serializer.data)
        return Response("No transactions", status=status.HTTP_404_NOT_FOUND)
