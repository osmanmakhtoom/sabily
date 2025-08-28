from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from apps.events.api.v1.serializers import SpeakerSerializerV1
from apps.events.models import Speaker


class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.filter(is_active=True)
    serializer_class = SpeakerSerializerV1
    permission_classes = (IsAdminUser,)
    http_method_names = ["get", "head", "options", "post", "put", "patch"]

    def get_serializer_class(self):
        if self.request.version == "v1":
            return SpeakerSerializerV1
        return super(SpeakerViewSet, self).get_serializer_class()

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [AllowAny()]
        return super(SpeakerViewSet, self).get_permissions()

    def get_view_name(self):
        return "Event Speakers"

    def get_view_description(self, html=False):
        return "Event Speakers Actions"

    @swagger_auto_schema(tags=["Event Speakers"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Event Speakers"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Event Speakers"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Event Speakers"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Event Speakers"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Event Speakers"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
