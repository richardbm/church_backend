from rest_framework.permissions import AllowAny

from apps.api.v1.church.serializers import AboutSerializer, ContactSerializer
from apps.api.v1.views import CustomViewSet
from apps.church.services import get_about, get_about_list, get_contact, get_contact_list


class AboutViewSet(CustomViewSet):
    serializer_class = AboutSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'about_id'
    detail_service = staticmethod(get_about)
    list_service = staticmethod(get_about_list)


class ContactViewSet(CustomViewSet):
    serializer_class = ContactSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'contact_id'
    detail_service = staticmethod(get_contact)
    list_service = staticmethod(get_contact_list)


class NewsViewSet(CustomViewSet):
    serializer_class = ContactSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'contact_id'
    detail_service = staticmethod(get_contact)
    list_service = staticmethod(get_contact_list)
