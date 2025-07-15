from django.contrib import admin
from .models import IPO

@admin.register(IPO)
class IPOAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'status', 'open_date', 'close_date', 'price_band', 'issue_size']
    list_filter = ['status', 'issue_type']
    search_fields = ['company_name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = [
        ('Basic Information', {
            'fields': ['company_name', 'company_logo', 'status', 'issue_type']
        }),
        ('Price Information', {
            'fields': [('price_band_lower', 'price_band_upper'), 'issue_size', 
                      'ipo_price', 'listing_price', 'current_market_price']
        }),
        ('Important Dates', {
            'fields': [('open_date', 'close_date'), 'listing_date']
        }),
        ('Documents', {
            'fields': ['rhp_document', 'drhp_document']
        }),
        ('System Fields', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        })
    ]
