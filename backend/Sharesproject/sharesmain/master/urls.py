from django.urls import path
from . import views

urlpatterns = [
    path("share",views.MainShareView.as_view({
        "post":"create",
        "get":"list"
    })),
    path("share/<int:pk>", views.MainShareView.as_view({
        "delete": "destroy",
        "get": "retrieve",
        "patch": "update",
    })),
    path("share/<int:pk>/archive", views.MainShareView.as_view({
        "get": "archive",
    })),
    path("share/user", views.UserMainShareView.as_view({
        "get": "list",
        "post": "create",
    })),
    path("share/user/<int:pk>", views.UserMainShareView.as_view({
        "delete": "destroy",
        "patch": "update",
        "get": "retrieve"
    })),
    path("share/watchlist", views.UserWatchlistView.as_view({
        "get": "list",
        "post": "create",
    })),
    path("share/watchlist/<int:pk>", views.UserMainShareView.as_view({
        "delete": "destroy",
        "patch": "update",
        "get": "retrieve"
    })),
]