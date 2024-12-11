from django.contrib import admin
from .models import Country, AnnualData, QuarterlyData

admin.site.register(Country)
admin.site.register(AnnualData)
admin.site.register(QuarterlyData)