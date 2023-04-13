
import json
from django.core.management.base import BaseCommand
from dashboard.models import Data
from datetime import datetime


def getdate(date_str):
    try:
        date_format = "%B, %d %Y %H:%M:%S"
        date_obj = datetime.strptime(date_str, date_format)
        return str(date_obj)
    except:
        return None

class Command(BaseCommand):
    help = 'Load data from json file'

    def handle(self, *args, **options):
        with open('dashboard/static/jsondata.json', 'r', encoding='utf-8') as f:
            data = json.load(f) 
            
            for item in data:   
                Data.objects.create( 
                    end_year = item['end_year'],
                    intensity = item['intensity'],
                    sector = item['sector'],
                    topic = item['topic'],
                    insight = item['insight'],
                    url = item['url'],
                    region = item['region'],
                    start_year = item['start_year'],
                    impact = item['impact'],
                    added = getdate(item['added']),
                    published = getdate(item['published']),
                    country = item['country'],
                    relevance = item['relevance'],
                    pestle = item['pestle'],
                    source = item['source'],
                    title = item['title'],
                    likelihood = item['likelihood'],
                    city = '',
                )