from rest_framework.permissions import AllowAny

from apps.ministries.services import get_ministry, get_ministries_list
from .serializers import MinistrySerializer
from ..views import CustomViewSet


class MinistriesViewSet(CustomViewSet):
    serializer_class = MinistrySerializer
    permission_classes = (AllowAny,)
    lookup_field = 'ministry_id'
    detail_service = staticmethod(get_ministry)
    list_service = staticmethod(get_ministries_list)
