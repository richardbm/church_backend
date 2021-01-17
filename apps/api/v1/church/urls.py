from django.urls import include, path
from rest_framework import routers

from apps.api.v1.church.views import AboutViewSet, ContactViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register("about", AboutViewSet, basename="about")
router.register("contacts", ContactViewSet, basename="contact")

urlpatterns = [path("", include(router.urls))]
