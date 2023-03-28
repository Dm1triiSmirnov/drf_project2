from django.urls import path

from wallet.views import (WalletsListCreateViewSet,
                          WalletsRetrieveDestroyViewSet)

urlpatterns = [
    path(
        "", WalletsListCreateViewSet.as_view({
            "get": "list", "post": "create"})
    ),
    path(
        "<str:name>/",
        WalletsRetrieveDestroyViewSet.as_view(
            {"get": "retrieve", "delete": "destroy"}
        ),
    ),
]
