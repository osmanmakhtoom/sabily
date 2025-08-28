from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from apps.events.api.v1.serializers import ProgramOrderSerializerV1
from apps.events.models import ProgramOrder


class ProgramOrderViewSet(viewsets.ModelViewSet):
    queryset = ProgramOrder.objects.filter(is_active=True)
    serializer_class = ProgramOrderSerializerV1
    permission_classes = (IsAdminUser,)
    http_method_names = ["get", "head", "options", "post", "put", "patch"]

    def get_serializer_class(self):
        if self.request.version == "v1":
            return ProgramOrderSerializerV1
        return super(ProgramOrderViewSet, self).get_serializer_class()

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [AllowAny()]
        return super(ProgramOrderViewSet, self).get_permissions()

    def get_view_name(self):
        return "Program Orders"

    def get_view_description(self, html=False):
        return "Program Orders Actions"

    @swagger_auto_schema(tags=["Program Orders"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Program Orders"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Program Orders"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Program Orders"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Program Orders"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Program Orders"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
