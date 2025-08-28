from django.core.exceptions import ImproperlyConfigured
from rest_framework import serializers

from apps.charity.models import CharityType


class CharityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityType
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


class CharityTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityType
        fields = (
            "id",
            "name",
            "icon",
        )

    def save(self, **kwargs):
        raise ImproperlyConfigured("CharityTypeListSerializer should not be called!")
