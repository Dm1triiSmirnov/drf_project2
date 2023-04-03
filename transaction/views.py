from rest_framework import viewsets, mixins


from transaction.models import Transaction
from transaction.serializers import TransactionSerializer


class TransactionListCreateViewSet(mixins.CreateModelMixin,
                                   mixins.ListModelMixin,
                                   viewsets.GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionRetrieveDestroyViewSet(mixins.RetrieveModelMixin,
                                        mixins.DestroyModelMixin,
                                        viewsets.GenericViewSet,):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
