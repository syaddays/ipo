from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from core.models import IPO

class Command(BaseCommand):
    help = 'Loads sample IPO data into the database'

    def handle(self, *args, **kwargs):
        # Clear existing IPOs
        IPO.objects.all().delete()
        
        # Base date for sample data
        base_date = timezone.now().date()
        
        sample_ipos = [
            {
                'company_name': 'TechCorp Solutions Ltd',
                'company_logo': 'https://placeholder.com/150',
                'price_band_lower': 850,
                'price_band_upper': 900,
                'issue_size': 1500.00,
                'issue_type': 'Book Built',
                'status': 'upcoming',
                'open_date': base_date + timedelta(days=15),
                'close_date': base_date + timedelta(days=17),
                'rhp_document': 'https://example.com/rhp.pdf',
                'drhp_document': 'https://example.com/drhp.pdf',
            },
            {
                'company_name': 'Green Energy Innovations',
                'company_logo': 'https://placeholder.com/150',
                'price_band_lower': 275,
                'price_band_upper': 290,
                'issue_size': 2000.00,
                'issue_type': 'Book Built',
                'status': 'open',
                'open_date': base_date,
                'close_date': base_date + timedelta(days=2),
                'rhp_document': 'https://example.com/rhp.pdf',
                'drhp_document': 'https://example.com/drhp.pdf',
            },
            {
                'company_name': 'HealthTech Pharma',
                'company_logo': 'https://placeholder.com/150',
                'price_band_lower': 1200,
                'price_band_upper': 1250,
                'issue_size': 3000.00,
                'issue_type': 'Book Built',
                'status': 'closed',
                'open_date': base_date - timedelta(days=10),
                'close_date': base_date - timedelta(days=8),
                'ipo_price': 1225,
                'rhp_document': 'https://example.com/rhp.pdf',
                'drhp_document': 'https://example.com/drhp.pdf',
            },
            {
                'company_name': 'Digital Payments Pro',
                'company_logo': 'https://placeholder.com/150',
                'price_band_lower': 450,
                'price_band_upper': 460,
                'issue_size': 1800.00,
                'issue_type': 'Book Built',
                'status': 'listed',
                'open_date': base_date - timedelta(days=30),
                'close_date': base_date - timedelta(days=28),
                'listing_date': base_date - timedelta(days=15),
                'ipo_price': 455,
                'listing_price': 550,
                'current_market_price': 575,
                'rhp_document': 'https://example.com/rhp.pdf',
                'drhp_document': 'https://example.com/drhp.pdf',
            },
            {
                'company_name': 'Consumer Retail Plus',
                'company_logo': 'https://placeholder.com/150',
                'price_band_lower': 350,
                'price_band_upper': 375,
                'issue_size': 2500.00,
                'issue_type': 'Book Built',
                'status': 'listed',
                'open_date': base_date - timedelta(days=45),
                'close_date': base_date - timedelta(days=43),
                'listing_date': base_date - timedelta(days=30),
                'ipo_price': 375,
                'listing_price': 400,
                'current_market_price': 425,
                'rhp_document': 'https://example.com/rhp.pdf',
                'drhp_document': 'https://example.com/drhp.pdf',
            },
        ]

        for ipo_data in sample_ipos:
            IPO.objects.create(**ipo_data)
            self.stdout.write(self.style.SUCCESS(f'Created IPO: {ipo_data["company_name"]}')) 