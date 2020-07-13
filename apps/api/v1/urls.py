from django.urls import include, path

app_name = "api"

urlpatterns = [
    path(r"accounts/", include("apps.api.v1.accounts.urls", namespace="accounts")),
    path(r"church/", include("apps.api.v1.church.urls", namespace="church")),
]
