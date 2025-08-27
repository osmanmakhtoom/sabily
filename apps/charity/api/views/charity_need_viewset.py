from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from apps.charity.models import CharityNeed
from apps.charity.api.v1.serializers import CharityNeedSerializerV1


class CharityNeedViewSet(viewsets.ModelViewSet):
    queryset = CharityNeed.objects.filter(is_active=True)
    serializer_class = CharityNeedSerializerV1
    permission_classes = (IsAdminUser,)
    http_method_names = ["get", "head", "options", "post", "put", "patch"]

    def get_serializer_class(self):
        if self.request.version == "v1":
            return CharityNeedSerializerV1
        return super(CharityNeedViewSet, self).get_serializer_class()

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [AllowAny()]
        return super(CharityNeedViewSet, self).get_permissions()

    def get_view_name(self):
        return "Charity Needs"

    def get_view_description(self, html=False):
        return "Charity Needs Actions"

    @swagger_auto_schema(tags=["Charity Needs"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Charity Needs"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Charity Needs"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Charity Needs"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Charity Needs"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Charity Needs"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
