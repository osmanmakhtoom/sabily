from rest_framework import serializers

from apps.events.models import ProgramOrder


class ProgramOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramOrder
        fields = "__all__"
