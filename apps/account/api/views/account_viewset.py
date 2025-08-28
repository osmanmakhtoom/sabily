from django.contrib.auth.hashers import make_password
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.account.models import User
from apps.account.api.v1.serializers import (
    UserSerializerV1,
    UserProfileSerializerV1,
    UserAddressesSerializerV1,
    UserChangeActivationSerializerV1,
)
from utils.bases.paginated_response import create_paginated_response_serializer
from utils.permissions import IsSuperUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(deleted=False)
    serializer_class = UserSerializerV1
    permission_classes = (permissions.IsAdminUser,)
    lookup_field = "id"
    http_method_names = ["get", "post", "delete", "patch", "put"]

    def get_serializer_class(self):
        if self.request.version == "v1":
            return UserSerializerV1
        return super().get_serializer_class()

    def get_view_name(self):
        return "Users"

    def get_view_description(self, html=False):
        return "Account and Users Actions"

    @swagger_auto_schema(
        tags=["Users"],
        operation_summary="Get Users",
        operation_description="Get Users",
        operation_id="get_users",
        responses={200: create_paginated_response_serializer(UserSerializerV1)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Users"],
        operation_summary="Get User",
        operation_description="Get User",
        operation_id="get_user",
        responses={200: UserSerializerV1()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Users"],
        operation_summary="Deactivate User",
        operation_description="Deactivate User",
        operation_id="deactivate_user",
        responses={200: UserSerializerV1()},
        request_body=UserChangeActivationSerializerV1,
    )
    @action(
        detail=True,
        methods=["patch"],
        url_path="deactivate-user",
        permission_classes=[permissions.IsAdminUser, IsSuperUser],
    )
    def deactivate_user(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = request.data.get("is_active", False)
        user.save(update_fields=["is_active"])
        return Response(UserSerializerV1(instance=user).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["Users"],
        operation_summary="Destroy User",
        operation_description="Destroy User",
        operation_id="destroy_user",
    )
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        method="get",
        operation_description="Get current logged-in user's info.",
        operation_summary="Current User",
        operation_id="get_current_user",
        responses={200: UserSerializerV1()},
        tags=["Users"],
    )
    @action(
        detail=False,
        methods=["get"],
        url_path="me",
        permission_classes=[permissions.IsAuthenticated],
    )
    def me(self, request):
        return Response(self.get_serializer(request.user).data)

    @swagger_auto_schema(
        method="post",
        operation_description="Register a new user.",
        operation_summary="Register User",
        operation_id="register_user",
        request_body=UserSerializerV1(),
        responses={201: UserSerializerV1()},
        tags=["Users"],
    )
    @action(
        detail=False,
        methods=["post"],
        permission_classes=[permissions.AllowAny],
        url_path="register",
    )
    def register(self, request):
        data = request.data.copy()
        data["password"] = make_password(data.get("password"))
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(self.get_serializer(user).data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        method="post",
        operation_description="Reset password for a user.",
        operation_summary="Reset Password",
        operation_id="reset_user_password",
        manual_parameters=[
            openapi.Parameter(
                "user_id", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True
            ),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["new_password"],
            properties={
                "new_password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        tags=["Users"],
    )
    @action(
        detail=False,
        methods=["post"],
        permission_classes=[permissions.IsAdminUser, IsSuperUser],
        url_path="reset-password",
    )
    def reset_password(self, request):
        user_id = request.query_params.get("user_id")
        new_password = request.data.get("new_password")

        if not user_id or not new_password:
            return Response(
                {"detail": "user_id and new_password are required."}, status=400
            )

        try:
            user = User.objects.get(id=user_id)
            user.password = make_password(new_password)
            user.save()
            return Response({"detail": "Password reset successfully."}, status=200)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=404)

    @swagger_auto_schema(
        method="post",
        tags=["Users"],
        request_body=UserAddressesSerializerV1(),
        operation_summary="Add address",
        operation_description="Add address to current user",
        operation_id="add_address",
        responses={201: UserAddressesSerializerV1()},
    )
    @action(
        detail=False,
        methods=["post"],
        url_path="add-address",
        permission_classes=[permissions.IsAuthenticated],
    )
    def add_address(self, request):
        serializer = UserAddressesSerializerV1(data=request.data)
        serializer.is_valid(raise_exception=True)
        address = serializer.save(user=request.user)
        return Response(
            UserAddressesSerializerV1(address).data, status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @swagger_auto_schema(auto_schema=None)
    def create(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @swagger_auto_schema(
        method="put",
        tags=["Users"],
        request_body=UserProfileSerializerV1(),
        operation_summary="Edit profile",
        operation_description="Edit current users profile",
        operation_id="edit_profile",
        responses={200: UserProfileSerializerV1()},
    )
    @action(
        detail=False,
        methods=["put"],
        url_path="edit-profile",
        permission_classes=[permissions.IsAuthenticated],
    )
    def edit_profile(self, request):
        profile = request.user.userprofile
        serializer = UserProfileSerializerV1(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
