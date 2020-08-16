from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.ministries.services import get_ministry, get_ministries_list
from .serializers import MinistrySerializer


class MinistriesViewSet(ViewSet):
    serializer_class = MinistrySerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, pk=None):
        ministry = get_ministry(ministry_id=pk)
        if not ministry:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(instance=ministry)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        queryset = get_ministries_list()
        serializer = self.serializer_class(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
