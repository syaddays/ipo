from rest_framework import serializers
from .models import IPO

class IPOSerializer(serializers.ModelSerializer):
    listing_gain = serializers.FloatField(read_only=True)
    current_return = serializers.FloatField(read_only=True)
    price_band = serializers.CharField(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = IPO
        fields = [
            'id', 'company_name', 'company_logo', 'price_band',
            'price_band_lower', 'price_band_upper', 'issue_size',
            'issue_type', 'status', 'status_display',
            'open_date', 'close_date', 'listing_date',
            'ipo_price', 'listing_price', 'current_market_price',
            'listing_gain', 'current_return',
            'rhp_document', 'drhp_document',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at'] 