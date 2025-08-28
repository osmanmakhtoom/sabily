from rest_framework import serializers


def create_paginated_response_serializer(serializer_class: serializers.BaseSerializer):
    class PaginatedResponse(serializers.Serializer):
        count = serializers.IntegerField()
        next = serializers.URLField(allow_null=True)
        previous = serializers.URLField(allow_null=True)
        results = serializer_class(many=True)

    return PaginatedResponse
