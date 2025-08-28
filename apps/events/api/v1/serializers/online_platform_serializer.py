from rest_framework import serializers

from apps.events.models import OnlinePlatform


class OnlinePlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlinePlatform
        fields = "__all__"
