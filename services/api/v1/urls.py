from django.urls import path
from services.api.v1.viewsets import PickDropView


urlpatterns = [
    path('pick_drop/', PickDropView.as_view(), name="pick_drop")
]
