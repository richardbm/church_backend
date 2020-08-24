from django.urls import include, path

app_name = "api"

urlpatterns = [
    path(r"accounts/", include("apps.api.v1.accounts.urls", namespace="accounts")),
    path(r"church/", include("apps.api.v1.church.urls", namespace="church")),
    path(r"ministries/", include("apps.api.v1.ministries.urls", namespace="ministries")),
    path(r"events/", include("apps.api.v1.events.urls", namespace="events")),
]
