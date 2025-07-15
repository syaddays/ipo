from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class IPO(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('listed', 'Listed'),
    ]

    # Basic Information
    company_name = models.CharField(max_length=200)
    company_logo = models.URLField(null=True, blank=True, help_text='URL to company logo')
    
    # Price Information
    price_band_lower = models.DecimalField(max_digits=10, decimal_places=2)
    price_band_upper = models.DecimalField(max_digits=10, decimal_places=2)
    issue_size = models.DecimalField(max_digits=20, decimal_places=2, help_text='Issue size in Crores')
    
    # Issue Type and Status
    issue_type = models.CharField(max_length=50, help_text='e.g., Book Built, Fixed Price')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    
    # Important Dates
    open_date = models.DateField()
    close_date = models.DateField()
    listing_date = models.DateField(null=True, blank=True)
    
    # Price Information
    ipo_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, 
                                  help_text='Final IPO price')
    listing_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_market_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Documents
    rhp_document = models.URLField(null=True, blank=True, help_text='URL to Red Herring Prospectus')
    drhp_document = models.URLField(null=True, blank=True, help_text='URL to Draft Red Herring Prospectus')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def listing_gain(self):
        """Calculate listing gain/loss percentage"""
        if self.listing_price and self.ipo_price and self.ipo_price > 0:
            return ((self.listing_price - self.ipo_price) / self.ipo_price) * 100
        return None

    @property
    def current_return(self):
        """Calculate current return percentage"""
        if self.current_market_price and self.ipo_price and self.ipo_price > 0:
            return ((self.current_market_price - self.ipo_price) / self.ipo_price) * 100
        return None

    @property
    def price_band(self):
        """Return formatted price band"""
        return f"₹{self.price_band_lower} - ₹{self.price_band_upper}"

    def __str__(self):
        return f"{self.company_name} - {self.get_status_display()}"

    class Meta:
        ordering = ['-open_date']
        verbose_name = 'IPO'
        verbose_name_plural = 'IPOs'
