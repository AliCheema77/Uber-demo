from django.template.defaultfilters import lower
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from services.api.v1.serializers import PickDropSerializer
from rest_framework.views import APIView
from django.db.models import Q
from users.api.v1.serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from services.models import RiderRequest
from services.api.v1.serializers import RiderRequestSerializer

User = get_user_model()


class PickDropView(APIView):
    serializer_class = PickDropSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            local_drivers = []
            pick = lower(serializer.validated_data["pick"])
            destination = lower(serializer.validated_data["destination"])
            drivers = User.objects.filter(account_type="drive_and_deliver")
            for driver in drivers:
                if lower(driver.city) in pick:
                    drivers_data = UserProfileSerializer(driver, many=False)
                    local_drivers.append(drivers_data.data)
            return Response({'drivers': local_drivers}, status=status.HTTP_200_OK)
        return Response({'error': "there is error"}, status=status.HTTP_400_BAD_REQUEST)


class RiderRequestView(APIView):
    serializer_class = RiderRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"response": serializer.data}, status=status.HTTP_200_OK)
        return Response({"response": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)