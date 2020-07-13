from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from apps.api.v1.church.serializers import AboutSerializer
from apps.church.services import get_about, get_about_list


class AboutViewSet(ViewSet):
    serializer_class = AboutSerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, pk=None):
        about = get_about(about_id=pk)
        if not about:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(instance=about)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        queryset = get_about_list()
        serializer = self.serializer_class(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
