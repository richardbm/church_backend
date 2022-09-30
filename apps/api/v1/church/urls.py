from django.urls import include, path
from rest_framework import routers

from apps.api.v1.church.views import AboutViewSet, ContactViewSet, NewsViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register("about", AboutViewSet, basename="about")
router.register("contacts", ContactViewSet, basename="contact")
router.register("news", NewsViewSet, basename="news")

urlpatterns = [path("", include(router.urls))]
