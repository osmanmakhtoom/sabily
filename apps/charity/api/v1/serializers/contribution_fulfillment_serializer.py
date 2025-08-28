from rest_framework import serializers

from apps.charity.models import ContributionFulfillment


class ContributionFulfillmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributionFulfillment
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
