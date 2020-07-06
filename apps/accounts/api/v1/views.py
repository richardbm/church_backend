from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.accounts.api.v1.serializers import UserRegistrationSerializer


class UserRegistrationViewSet(ModelViewSet):
    http_method_names = ("post",)
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
