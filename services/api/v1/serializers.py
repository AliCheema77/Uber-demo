from rest_framework import serializers
from services.models import RiderRequest
from users.api.v1.serializers import UserProfileSerializer


class PickDropSerializer(serializers.Serializer):
    pick = serializers.CharField(max_length=255, required=True)
    destination = serializers.CharField(max_length=255, required=True)


class RiderRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = RiderRequest
        fields = ['id', 'destination_label', 'pickup_label', 'destination_coordinates', 'pickup_coordinates',
                  'status', 'requester', 'deriver']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["requester"] = {
            "id": instance.requester.id,
            "username": instance.requester.username,
            }
        data["deriver"] = {
            "id": instance.deriver.id,
            "username": instance.deriver.username,
            }
        return data


class DriverAcceptCancelRideSerializer(serializers.Serializer):
    request_id = serializers.IntegerField(required=True)
    status = serializers.CharField(max_length=5, required=True)
