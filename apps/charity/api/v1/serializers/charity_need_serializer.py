from rest_framework import serializers

from apps.charity.models import CharityNeed, CharityNeedMedia


class CharityNeedMediaListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CharityNeedMedia
        fields = (
            "id",
            "image",
        )

    def get_image(self, obj):
        return obj.image.url if obj.image else None


class CharityNeedSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = CharityNeed
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

    def get_images(self, obj):
        return CharityNeedMediaListSerializer(
            obj.images.all(), many=True, read_only=True
        ).data
