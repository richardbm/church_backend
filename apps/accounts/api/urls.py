from django.urls import include, path

app_name = "accounts"

urlpatterns = [
    path(r"accounts/", include("apps.accounts.api.v1.urls", namespace="accounts")),
]
