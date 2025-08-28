from django.core.exceptions import ImproperlyConfigured
from rest_framework import serializers

from apps.charity.api.v1.serializers.charity_type_serializer import (
    CharityTypeListSerializer,
)
from apps.charity.api.v1.serializers.donation_item_type_serializer import (
    DonationItemTypeListSerializer,
)
from apps.charity.models import Charity


class CharitySerializer(serializers.ModelSerializer):
    charity_types = CharityTypeListSerializer(many=True, read_only=True)
    accepts_donation_types = DonationItemTypeListSerializer(many=True, read_only=True)

    class Meta:
        model = Charity
        fields = "__all__"
        read_only_fields = (
            "id",
            "is_active",
            "is_verified",
            "verified_by",
            "verified_at",
            "deleted",
            "deleted_at",
            "created_at",
            "updated_at",
        )


class CharityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = (
            "id",
            "name",
            "website",
            "logo",
        )

    def save(self, **kwargs):
        raise ImproperlyConfigured("CharityListSerializer should not be called!")
