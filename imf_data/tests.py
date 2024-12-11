from django.test import TestCase
from rest_framework.test import APIClient
from .models import Country, AnnualData, QuarterlyData
from .serializers import CountrySerializer, AnnualDataSerializer, QuarterlyDataSerializer

class ModelTests(TestCase):
    def setUp(self):
        self.country = Country.objects.create(country="United States")
        self.annual_data = AnnualData.objects.create(
            country=self.country,
            metric="GDP",
            year=2022,
            value=21433225.0
        )
        self.quarterly_data = QuarterlyData.objects.create(
            country=self.country,
            metric="GDP",
            year=2022,
            quarter="1",
            value=5321456.25
        )

    def test_country_model(self):
        self.assertEqual(str(self.country), "United States")

    def test_annual_data_model(self):
        self.assertEqual(str(self.annual_data), "United States - GDP (2022)")

    def test_quarterly_data_model(self):
        self.assertEqual(str(self.quarterly_data), "United States - GDP (2022 Q1)")

class SerializerTests(TestCase):
    def setUp(self):
        self.country = Country.objects.create(country="United States")
        self.country_data = {"country": "Canada"}
        self.annual_data = {
            "country": self.country.country_id,
            "metric": "GDP",
            "year": 2022,
            "value": 21433225.0
        }
        self.quarterly_data = {
            "country": self.country.country_id,
            "metric": "GDP",
            "year": 2022,
            "quarter": "1",
            "value": 5321456.25
        }

    def test_country_serializer(self):
        serializer = CountrySerializer(data=self.country_data)
        self.assertTrue(serializer.is_valid())

    def test_annual_data_serializer(self):
        serializer = AnnualDataSerializer(data=self.annual_data)
        self.assertTrue(serializer.is_valid())

    def test_quarterly_data_serializer(self):
        serializer = QuarterlyDataSerializer(data=self.quarterly_data)
        self.assertTrue(serializer.is_valid())

class ViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.country = Country.objects.create(country="United States")
        self.annual_data = AnnualData.objects.create(
            country=self.country,
            metric="GDP",
            year=2022,
            value=21433225.0
        )
        self.quarterly_data = QuarterlyData.objects.create(
            country=self.country,
            metric="GDP",
            year=2022,
            quarter="1",
            value=5321456.25
        )

    def test_get_countries(self):
        response = self.client.get('/api/countries/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_annual_data(self):
        response = self.client.get('/api/annual-data/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_quarterly_data(self):
        response = self.client.get('/api/quarterly-data/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

