from django.urls import include, path

app_name = "accounts"

urlpatterns = [
    path(r"v1/", include("apps.accounts.api.urls", namespace="api")),
]
