from rest_framework import serializers
from .models import Country, AnnualData, QuarterlyData

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_id', 'country']

class AnnualDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualData
        fields = ['annual_id', 'country', 'metric', 'year', 'value']

class QuarterlyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyData
        fields = ['quarter_id', 'country', 'metric', 'year', 'quarter', 'value']