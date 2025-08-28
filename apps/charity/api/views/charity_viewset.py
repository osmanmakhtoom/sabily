from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from apps.charity.models import Charity
from apps.charity.api.v1.serializers import CharitySerializerV1


class CharityViewSet(viewsets.ModelViewSet):
    queryset = Charity.objects.filter(is_active=True)
    serializer_class = CharitySerializerV1
    permission_classes = (IsAdminUser,)
    http_method_names = ["get", "head", "options", "post", "put", "patch"]

    def get_serializer_class(self):
        if self.request.version == "v1":
            return CharitySerializerV1
        return super(CharityViewSet, self).get_serializer_class()

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [AllowAny()]
        return super(CharityViewSet, self).get_permissions()

    def get_view_name(self):
        return "Charities"

    def get_view_description(self, html=False):
        return "Charities Actions"

    @swagger_auto_schema(tags=["Charities"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Charities"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Charities"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Charities"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Charities"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Charities"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
