from rest_framework import serializers

from apps.charity.models import CashContribution


class CashContributionMinifiedSerializer(serializers.ModelSerializer):
    contribution_type = serializers.CharField(source="contribution_type.name")
    charity = serializers.CharField(source="charity.name")

    class Meta:
        model = CashContribution
        fields = [
            "contribution_type",
            "amount",
            "currency",
            "charity",
            "is_verified",
            "status",
        ]


class CashContributionSerializer(CashContributionMinifiedSerializer):
    verified_by = serializers.SerializerMethodField()
    user = serializers.CharField(source="user.full_name")

    class Meta:
        model = CashContribution
        fields = CashContributionMinifiedSerializer.Meta.fields + [
            "id",
            "verified_by",
            "user",
            "is_active",
            "created_at",
        ]

    def get_verified_by(self, obj):
        return obj.verified_by.full_name if obj.verified_by else None


class CashContributionDetailSerializer(serializers.ModelSerializer):
    verified_by = serializers.SerializerMethodField()
    user = serializers.CharField(source="user.full_name")
    charity = serializers.CharField(source="charity.name")
    contribution_type = serializers.CharField(source="contribution_type.name")

    class Meta:
        model = CashContribution
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
            "status",
            "date_confirmed",
        )

    def get_verified_by(self, obj):
        return obj.verified_by.full_name if obj.verified_by else None
