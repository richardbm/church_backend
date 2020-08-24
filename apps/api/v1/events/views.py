from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.events.services import get_event_occurrences
from .serializers import OccurrenceSerializer


class OccurrenceViewSet(ViewSet):
    serializer_class = OccurrenceSerializer
    permission_classes = (AllowAny,)

    def list(self, request):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")
        ministry_id = request.query_params.get("ministry_id")
        if not start_date:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error_message": "start_date date is required"},
            )
        if not end_date:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error_message": "end_date date is required"},
            )

        occurrences = get_event_occurrences(start_date, end_date, ministry_id)
        serializer = self.serializer_class(instance=occurrences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
