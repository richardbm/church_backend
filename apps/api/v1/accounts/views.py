from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from apps.accounts.services import create_user
from apps.api.v1.accounts.serializers import UserRegistrationSerializer


class UserRegistrationViewSet(ViewSet):
    http_method_names = ("post",)
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        data["username"] = data["email"]
        user = create_user(data)
        data = self.serializer_class(user).data
        return Response(data, status=status.HTTP_201_CREATED)
