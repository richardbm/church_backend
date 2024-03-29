from django.urls import include, path
from rest_framework import routers

from apps.api.v1.accounts.views import UserRegistrationViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register("registration", UserRegistrationViewSet, basename="registration")

urlpatterns = [path("", include(router.urls))]
