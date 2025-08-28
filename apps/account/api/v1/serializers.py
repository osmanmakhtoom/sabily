from rest_framework import serializers

from apps.account.models import User, UserProfile, UserAddress


class UserProfileSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "bio",
            "profile_picture",
            "cover_photo",
            "social_links",
        )


class UserAddressesSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = (
            "phone_number",
            "country",
            "province",
            "city",
            "street",
            "postal_code",
            "longitude",
            "latitude",
            "is_default",
        )


class UserSerializerV1(serializers.ModelSerializer):
    userprofile = UserProfileSerializerV1(read_only=True)
    addresses = UserAddressesSerializerV1(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "phone_number",
            "first_name",
            "last_name",
            "password",
            "is_active",
            "gender",
            "last_login",
            "userprofile",
            "addresses",
        )
        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
            "phone_number": {"required": True},
            "id": {"read_only": True},
            "password": {"required": True, "write_only": True},
            "last_login": {"read_only": True},
        }


class UserChangeActivationSerializerV1(serializers.Serializer):
    is_active = serializers.BooleanField()
