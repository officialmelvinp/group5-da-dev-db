from django.shortcuts import render
from rest_framework import viewsets
from .models import Country, AnnualData, QuarterlyData
from .serializers import CountrySerializer, AnnualDataSerializer, QuarterlyDataSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class AnnualDataViewSet(viewsets.ModelViewSet):
    queryset = AnnualData.objects.all()
    serializer_class = AnnualDataSerializer

class QuarterlyDataViewSet(viewsets.ModelViewSet):
    queryset = QuarterlyData.objects.all()
    serializer_class = QuarterlyDataSerializer

# Keeping existing views.
def country_list(request):
    countries = Country.objects.all()
    return render(request, 'imf_data/country_list.html', {'countries': countries})