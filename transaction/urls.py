from django.urls import path

from transaction.views import TransactionViewSet

urlpatterns = [
    path("", TransactionViewSet.as_view({"get": "list"})),
    # path(
    #     "<str:name>/",
    #     TransactionViewSet.as_view({"get": "list"}),
]
