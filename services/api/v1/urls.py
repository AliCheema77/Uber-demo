from django.urls import path
from services.api.v1.viewsets import PickDropView, RiderRequestView


urlpatterns = [
    path('pick_drop/', PickDropView.as_view(), name="pick_drop"),
    path('rider_request/', RiderRequestView.as_view(), name="rider_request"),
]
