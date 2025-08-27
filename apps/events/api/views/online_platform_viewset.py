from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from apps.events.api.v1.serializers import OnlinePlatformSerializerV1
from apps.events.models import OnlinePlatform


class OnlinePlatformViewSet(viewsets.ModelViewSet):
    queryset = OnlinePlatform.objects.filter(is_active=True)
    serializer_class = OnlinePlatformSerializerV1
    permission_classes = (IsAdminUser,)
    http_method_names = ["get", "head", "options", "post", "put", "patch"]

    def get_serializer_class(self):
        if self.request.version == "v1":
            return OnlinePlatformSerializerV1
        return super(OnlinePlatformViewSet, self).get_serializer_class()

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [AllowAny()]
        return super(OnlinePlatformViewSet, self).get_permissions()

    def get_view_name(self):
        return "Online Platforms"

    def get_view_description(self, html=False):
        return "Online Platforms Actions"

    @swagger_auto_schema(tags=["Online Platforms"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Online Platforms"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Online Platforms"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Online Platforms"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Online Platforms"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Online Platforms"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
