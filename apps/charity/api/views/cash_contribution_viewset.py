from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser

from apps.charity.models import CashContribution
from apps.charity.api.v1.serializers import (
    CashContributionSerializerV1,
    CashContributionDetailSerializerV1,
)


class CashContributionViewSet(viewsets.ModelViewSet):
    queryset = CashContribution.objects.filter(is_active=True)
    permission_classes = (IsAdminUser,)
    pagination_class = PageNumberPagination
    http_method_names = ["get", "head", "options", "post", "put", "patch"]

    def get_serializer_class(self):
        if self.request.version == "v1":
            if self.action == "list":
                return CashContributionSerializerV1
            elif self.action == "retrieve":
                return CashContributionSerializerV1
            return CashContributionDetailSerializerV1

        return CashContributionSerializerV1

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [AllowAny()]
        return super(CashContributionViewSet, self).get_permissions()

    def get_view_name(self):
        return "Cash Contributions"

    def get_view_description(self, html=False):
        return "Cash Contributions Actions"

    @swagger_auto_schema(
        tags=["Cash Contributions"],
        responses={200: CashContributionSerializerV1(many=True), 400: "Bad Request"},
        operation_description="List all cash contributions",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Cash Contributions"],
        responses={200: CashContributionDetailSerializerV1(), 404: "Not Found"},
        operation_description="Retrieve a cash contribution",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Cash Contributions"],
        request_body=CashContributionDetailSerializerV1,
        responses={201: CashContributionDetailSerializerV1(), 400: "Bad Request"},
        operation_description="Create a cash contribution",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Cash Contributions"],
        request_body=CashContributionDetailSerializerV1,
        responses={
            200: CashContributionDetailSerializerV1(),
            400: "Bad Request",
            404: "Not Found",
        },
        operation_description="Update a cash contribution",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Cash Contributions"],
        request_body=CashContributionDetailSerializerV1,
        responses={
            200: CashContributionDetailSerializerV1(),
            400: "Bad Request",
            404: "Not Found",
        },
        operation_description="Patch a cash contribution",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Cash Contributions"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
