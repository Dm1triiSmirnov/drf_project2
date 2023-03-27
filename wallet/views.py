from django.shortcuts import render
from rest_framework import viewsets, generics

from wallet.models import Wallet
from wallet.serializers import WalletSerializer


# class WalletViewSet(viewsets.ModelViewSet):
#     queryset = Wallet.objects.all()
#     serializer_class = WalletSerializer

class WalletAPIView(generics.ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
