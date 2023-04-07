from django.urls import path

from transaction.views import (
    TransactionListAPIView,
    TransactionListCreateViewSet,
    TransactionRetrieveViewSet,
)

urlpatterns = [
    path("", TransactionListCreateViewSet.as_view(
        {"get": "list", "post": "create"}
    )
         ),
    path(
        "<int:pk>/",
        TransactionRetrieveViewSet.as_view({"get": "retrieve"})),
    path("<str:pk>/", TransactionListAPIView.as_view()),
]
