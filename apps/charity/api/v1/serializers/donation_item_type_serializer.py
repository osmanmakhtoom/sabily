from django.core.exceptions import ImproperlyConfigured
from rest_framework import serializers

from apps.charity.models import DonationItemType


class DonationItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationItemType
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


class DonationItemTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationItemType
        fields = ("id", "name", "category", "unit", "icon", "is_acceptable")

    def save(self, **kwargs):
        raise ImproperlyConfigured(
            "DonationItemTypeListSerializer should not be called!"
        )
