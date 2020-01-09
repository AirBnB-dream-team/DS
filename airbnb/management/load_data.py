from django.core.management.base import BaseCommand, CommandError
from optimal_price.models import User 
import requests as request
import random
import datetime
import html2text
import faster_than_requests as requests
import json


class Command(BaseCommand):
    help = 'load data'

    # def add_arguments(self, parser):
    #     parser.add_argument('path', nargs=2, type=str)

    def handle(self, *args, **options):
        User.objects.all().delete()
    
        print("loading data from Hacker News api... ")

        url = 'https://saveonairbnb.herokuapp.com'

        count = 0
        for i in range(0, req):
            response = requests.get2json(f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty')
            count+=1
            print(i, count)
            data = json.loads(response) 
        
                print('inserting into database')
                '''
                Checking keys should be easier than this so maybe this can be a function. 
                '''
                User.objects.create(
                id = data['id'],
                by = data['by'],
                text = text_conv,
            )
            else:
                print('nope')