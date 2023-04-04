from rest_framework import mixins, viewsets, permissions, status
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


class TransactionRetrieveDestroyViewSet(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# class TransactionListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
#     lookup_fields = ["sender", "receiver"]

class TransactionListAPIView(ListAPIView):
    serializer_class = TransactionSerializer

    def get(self, request, *args, **kwargs) -> Response:
        # sender = self.request.query_params.get('pk')
        # receiver = self.request.query_params.get('pk')
        # user = self.request.query_params.get('user')
        #
        # queryset = Transaction.objects.filter(
        #     Q(sender__name=sender) | Q(receiver__name=receiver),
        #     Q(sender__user=user) | Q(receiver__user=user)
        # )

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