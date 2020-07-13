from django.urls import include, path
from rest_framework import routers

from apps.api.v1.church.views import AboutViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register("about", AboutViewSet, basename="about")

urlpatterns = [path("", include(router.urls))]
