from rest_framework import serializers

from apps.charity.models import GoodsContribution


class GoodsContributionMinifiedSerializer(serializers.ModelSerializer):
    charity = serializers.CharField(source="charity.name")
    item_type = serializers.CharField(source="item_type.name")

    class Meta:
        model = GoodsContribution
        fields = [
            "item_type",
            "charity",
            "is_verified",
            "quantity",
            "tracking_number",
            "status",
        ]


class GoodsContributionSerializer(GoodsContributionMinifiedSerializer):
    verified_by = serializers.SerializerMethodField()
    user = serializers.CharField(source="user.full_name")

    class Meta:
        model = GoodsContribution
        fields = GoodsContributionMinifiedSerializer.Meta.fields + [
            "id",
            "verified_by",
            "user",
            "is_active",
            "created_at",
        ]

    def get_verified_by(self, obj):
        return obj.verified_by.full_name if obj.verified_by else None


class GoodsContributionDetailSerializer(serializers.ModelSerializer):
    verified_by = serializers.SerializerMethodField()
    user = serializers.CharField(source="user.full_name")
    charity = serializers.CharField(source="charity.name")
    item_type = serializers.CharField(source="item_type.name")

    class Meta:
        model = GoodsContribution
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
