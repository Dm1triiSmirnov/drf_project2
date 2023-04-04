from django.urls import path

from transaction.views import (TransactionListCreateViewSet,
                               TransactionListViewSet,
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
        "<str:sender>/<str:receiver>/",
        TransactionListViewSet.as_view({"get": "list"})
    ),
]
