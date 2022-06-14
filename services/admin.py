from django.contrib import admin
from services.models import RiderRequest


@admin.register(RiderRequest)
class RiderRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'destination_label', 'pickup_label', 'destination_coordinates', 'pickup_coordinates',
                    'status', 'requester', 'deriver', 'updated_at', 'created_at']
