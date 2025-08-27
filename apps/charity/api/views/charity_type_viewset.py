from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from apps.charity.models import CharityType
from apps.charity.api.v1.serializers import CharityTypeSerializerV1


class CharityTypeViewSet(viewsets.ModelViewSet):
    queryset = CharityType.objects.filter(is_active=True)
    serializer_class = CharityTypeSerializerV1
    permission_classes = (IsAdminUser,)
    http_method_names = ["get", "head", "options", "post", "put", "patch"]

    def get_serializer_class(self):
        if self.request.version == "v1":
            return CharityTypeSerializerV1
        return super(CharityTypeViewSet, self).get_serializer_class()

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [AllowAny()]
        return super(CharityTypeViewSet, self).get_permissions()

    def get_view_name(self):
        return "Charity Types"

    def get_view_description(self, html=False):
        return "Charity Types Actions"

    @swagger_auto_schema(tags=["CharityTypes"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["CharityTypes"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["CharityTypes"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=["CharityTypes"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["CharityTypes"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["CharityTypes"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
