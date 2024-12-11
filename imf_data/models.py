from django.db import models
from django.core.exceptions import ValidationError

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name_plural = "countries"

class AnnualData(models.Model):
    annual_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='annual_data')
    metric = models.CharField(max_length=500)
    year = models.IntegerField()
    value = models.DecimalField(max_digits=15, decimal_places=2)
    
    class Meta:
        indexes = [
            models.Index(fields=['country', 'year']),
            models.Index(fields=['metric']),
        ]
    
    def clean(self):
        if self.year < 1900 or self.year > 2100:
            raise ValidationError('Year must be between 1900 and 2100')

    def __str__(self):
        return f"{self.country} - {self.metric} ({self.year})"

class QuarterlyData(models.Model):
    quarter_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='quarterly_data')
    metric = models.CharField(max_length=500)
    year = models.IntegerField(default=2000)  # Add a default value
    quarter = models.CharField(max_length=10)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    
    class Meta:
        indexes = [
            models.Index(fields=['country', 'year']),
            models.Index(fields=['metric']),
        ]
        verbose_name_plural = "quarterly data"

    def __str__(self):
        return f"{self.country} - {self.metric} ({self.year} Q{self.quarter})"

    def clean(self):
        if self.year < 1900 or self.year > 2100:
            raise ValidationError('Year must be between 1900 and 2100')