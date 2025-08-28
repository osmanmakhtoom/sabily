from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from apps.events.api.v1.serializers import ResourceSerializerV1
from apps.events.models import Resource


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.filter(is_active=True)
    serializer_class = ResourceSerializerV1
    permission_classes = (IsAdminUser,)
    http_method_names = ["get", "head", "options", "post", "put", "patch"]

    def get_serializer_class(self):
        if self.request.version == "v1":
            return ResourceSerializerV1
        return super(ResourceViewSet, self).get_serializer_class()

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [AllowAny()]
        return super(ResourceViewSet, self).get_permissions()

    def get_view_name(self):
        return "Event Resources"

    def get_view_description(self, html=False):
        return "Event Resources Actions"

    @swagger_auto_schema(tags=["Event Resources"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Event Resources"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Event Resources"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Event Resources"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Event Resources"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Event Resources"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
