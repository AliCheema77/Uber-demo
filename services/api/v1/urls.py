from django.urls import path
from services.api.v1.viewsets import PickDropView, RiderRequestView, RideRequestView, CancelRideView


urlpatterns = [
    path('pick_drop/', PickDropView.as_view(), name="pick_drop"),
    path('rider_request/', RiderRequestView.as_view(), name="rider_request"),
    path('requests/', RideRequestView.as_view(), name="request"),
    path('cancel_ride/<int:id>/', CancelRideView.as_view(), name="cancel_ride")
]
