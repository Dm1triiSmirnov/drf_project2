from django.urls import path

from transaction.views import (TransactionListCreateViewSet,
                               TransactionListAPIView,
                               TransactionRetrieveDestroyViewSet)

urlpatterns = [
    path("", TransactionListCreateViewSet.as_view({"get": "list",
                                                   "post": "create"})),
    path(
        "<int:pk>/",
        TransactionRetrieveDestroyViewSet.as_view(
            {"get": "retrieve", "delete": "destroy"}
        ),
    ),
    path(
        "<str:pk>/",
        TransactionListAPIView.as_view()
    ),
]
