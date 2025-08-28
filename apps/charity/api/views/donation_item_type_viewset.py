from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from apps.charity.models import DonationItemType
from apps.charity.api.v1.serializers import DonationItemTypeSerializerV1


class DonationItemTypeViewSet(viewsets.ModelViewSet):
    queryset = DonationItemType.objects.filter(is_active=True)
    serializer_class = DonationItemTypeSerializerV1
    permission_classes = (IsAdminUser,)
    http_method_names = ["get", "head", "options", "post", "put", "patch"]

    def get_serializer_class(self):
        if self.request.version == "v1":
            return DonationItemTypeSerializerV1
        return super(DonationItemTypeViewSet, self).get_serializer_class()

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [AllowAny()]
        return super(DonationItemTypeViewSet, self).get_permissions()

    def get_view_name(self):
        return "Donation Item Types"

    def get_view_description(self, html=False):
        return "Donation Item Types Actions"

    @swagger_auto_schema(tags=["Donation Item Types"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Donation Item Types"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Donation Item Types"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Donation Item Types"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Donation Item Types"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Donation Item Types"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
