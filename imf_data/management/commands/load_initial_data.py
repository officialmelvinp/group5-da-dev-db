from django.core.management.base import BaseCommand
from imf_data.models import Country, AnnualData, QuarterlyData
import csv

class Command(BaseCommand):
    help = 'Load data from CSV files'

    def handle(self, *args, **options):
        # Example for loading country data
        with open('data/countries.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                Country.objects.create(country_id=row[0], country=row[1])
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded data'))