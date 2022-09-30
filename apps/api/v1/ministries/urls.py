from django.urls import include, path
from rest_framework import routers

from .views import MinistriesViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register("ministries", MinistriesViewSet, basename="ministries")

urlpatterns = [path("", include(router.urls))]
