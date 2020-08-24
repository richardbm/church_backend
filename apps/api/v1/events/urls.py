from django.urls import include, path
from rest_framework import routers

from .views import OccurrenceViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register("occurrences", OccurrenceViewSet, basename="occurrences")

urlpatterns = [path("", include(router.urls))]
