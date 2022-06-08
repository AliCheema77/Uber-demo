from rest_framework import serializers


class PickDropSerializer(serializers.Serializer):
    pick = serializers.CharField(max_length=255, required=True)
    destination = serializers.CharField(max_length=255, required=True)

