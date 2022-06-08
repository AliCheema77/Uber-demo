from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from services.api.v1.serializers import PickDropSerializer
from rest_framework.views import APIView
from django.db.models import Q
from users.api.v1.serializers import UserProfileSerializer


User = get_user_model()


class PickDropView(APIView):
    serializer_class = PickDropSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            pick = serializer.validated_data["pick"]
            destination = serializer.validated_data["destination"]
            drivers = User.objects.filter(account_type="drive_and_deliver")
            drivers = drivers.filter(Q(city__icontains=pick) | Q(city__icontains=destination))
            drivers_data = UserProfileSerializer(drivers, many=True)
            return Response({'drivers': drivers_data.data}, status=status.HTTP_200_OK)
        return Response({'error': "there is error"}, status=status.HTTP_400_BAD_REQUEST)

