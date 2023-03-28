from django.urls import path

from wallet.views import WalletViewSet

urlpatterns = [
    path("", WalletViewSet.as_view({"get": "list"})),
    # path("<str:name>/", WalletViewSet.as_view({"get": "list"})),
]
