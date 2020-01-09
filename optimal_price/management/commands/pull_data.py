from django.core.management.base import BaseCommand, CommandError
from optimal_price.models import User
import json
from random import choice, randint
import requests

class Command(BaseCommand):
    help = 'load data'

    # def add_arguments(self, parser):
    #     parser.add_argument('path', nargs=2, type=str)

    def handle(self, *args, **options):
        User.objects.all().delete()
    
        print("loading data from heroku api... ")

        rooms = [ 'Entire home/apt', 'Private room', 'Hotel room', 'Shared room' ]

        props = [
            'House', 'Guesthouse', 'Condominium', 'Guest suite', 'Apartment',
            'Townhouse', 'Bungalow', 'Loft', 'Other', 'Cabin',
            'Bed and breakfast', 'Campsite', 'Tent', 'Villa', 'Camper/RV',
            'Cottage', 'Tiny house', 'Farm stay', 'Serviced apartment',
            'Boutique hotel', 'Dome house', 'Bus', 'Tipi', 'Treehouse', 'Barn',
            'Boat', 'Hostel', 'Aparthotel', 'Yurt', 'Chalet', 'Houseboat',
            'Resort', 'Hotel', 'Earth house'
       ]

        hoods = [
            'East Downtown', 'SW Williamson Co.', 'Travis Heights', 'Zilker',
            'missing', 'West Campus', 'East Riverside', 'Clarksville',
            'Brentwood', 'Cherry Creek', 'Scofield Ridge', 'Bouldin Creek',
            'Tarrytown', 'Northwest Hills', 'McKinney', 'South Congress',
            'Hyde Park', 'Dawson', 'Galindo', 'Upper Boggy Creek',
            'Barton Hills', 'Rosedale', 'Angus Valley', 'South Lamar',
            'West Austin', 'Downtown', 'University of Texas', 'MLK & 183',
            'Allendale', 'Windsor Park', 'Highland', 'Wooten', 'Rollingwood',
            'Govalle', 'Holly', 'Cesar Chavez', 'Rosewood', 'St. Edwards',
            'West Congress', 'East Congress', 'Long Canyon', 'South Manchaca',
            'Georgian Acres', 'Hancock', 'Westlake Hills', 'South First',
            'Riverside Heights', 'Oak Hill', 'Old Enfield', 'Old West Austin',
            'North Loop', 'Montopolis', 'Parker Lane', 'North Shoal Creek',
            'Pecan Spings', 'Cherrywood', 'Sunset Valley',
            'Balcones Civic Association', 'Pleasant Valley', 'Mueller',
            'Barton Creek', 'St. Johns', 'Copperfield', 'Westgate', 'Anaheim',
            'Bull Creek', 'Mission District', 'Crestview', 'Steiner Ranch',
            'Anderson Mill', 'Meeks Bay', 'Circle C', 'Bryker Woods',
            'Windsor Hills', 'Rainey Street', 'Gracywoods', 'Avondale',
            'University Hills', 'Capitol Hill', 'Milwood',
            'Tuxedo Park/South Tuxedo Park/Buckhead Forest', 'Cat Mountian',
            'East Village', 'Venice', 'Mesa Park', 'Paradise Park',
            'Williamsburg', 'Tulum Centro', 'Walnut Creek', 'Balcony Woods',
            'Whittier', 'Telegraph Hill', 'Lamplight Village',
            'Lincoln Square', 'Island of Hawaiʻi', 'Central City',
            'Mount Pleasant', 'Sol', 'Central Business District', 'Kauaʻi',
            'Chinatown', 'Santa Clara', 'Mission Valley East',
            'South Lake Tahoe', 'Kingsbury', 'Gateway', 'Waikiki',
            'Newport Beach', 'Park West', 'Incline Village', 'Exarcheia',
            'Central Berkeley', 'East Boston', 'Westchester/Playa Del Rey',
            'Near Northeast/H Street Corridor', 'Kingman Park', 'Midtown East',
            'Oak Lawn', 'Spring Garden', 'Upper West Side', 'Midtown',
            'Edgewater', 'Little Italy/UIC', 'Dorchester', 'Ala Moana/Kakaako',
            'Springwoods', 'Zephyr Cove', 'Walworth', 'Ballard',
            'North Austin Civic Association', 'Chelsea', 'Sunny Isles Beach',
            'Lower Garden District', 'Glencoe Park', 'Revere',
            'Central Austin', 'Lakewood', 'Gold Coast', 'South Austin',
            'Mesa Village', 'East Riverside - Oltorf', 'South Yarra',
            'Bergen/Lafayette', 'Los Indios', 'Petworth', 'Canyon Mesa',
            'Four Points Centre', 'Pennsport', 'La Jolla', 'Culver City',
            'American University Park', 'Dollar Point/Ridgewood', 'Teravista',
            'Oak Forest', 'Hornsby Glen', 'Noe Valley', 'Sunnyvale',
            'Southpark Meadows', 'West Oak Hill', 'Quarry', 'Pioneer Crossing',
            'Greater South River City', 'Las Trillizas', 'Central Dallas',
            'LB of Islington', 'Bronzeville', 'Soulard', 'South Beach',
            'Rough Hollow', 'Richmond'
        ]

        zips = [
            '78702', '78729', '78704', '78748', '78705', '78759', '78741',
            '78703', '78757', '78749', '78727', '78731', '78758', '78744',
            '78751', '78722', '78733', '78725', '78701', '78721', '78723',
            '78752', '0', '78732', '78746', '78754', '78728', '78737',
            '78745', '78730', '78724', '78747', '78753', '78735', '78756',
            '78734', '78739', '78738', '78726', '78717', '78736', '78750',
            '78652', '78620', '78712', '78742', '78669', '78681', '78719',
            '78767', '78660', '78619', '78613', '78653'
        ]

        res = 'results'
        url = 'https://saveonairbnb.herokuapp.com'

        for i in range(1, 800):

            bedrooms = randint(1, 8)
            bathrooms = randint(1, 8)
            minimum_nights = randint(1,8)
            zipcode = choice(zips)
            host_neighbourhood = choice(hoods)
            property_type =  choice(props)
            room_type =  choice(rooms)
            
            data = {  

                'bedrooms' : bedrooms, 
                'bathrooms' : bathrooms, 
                'minimum_nights' : minimum_nights, 
                'zipcode': zipcode, 
                'host_neighbourhood' : host_neighbourhood,
                'property_type' : property_type,
                'room_type' : room_type
            }

            data = json.dumps(data)
            pred = requests.post(url, data)
            # print(f'Prediction On Insert {i} : { abs( pred.json()[res][res] ) }')

            User.objects.create(
                bedrooms = bedrooms,
                bathrooms = bathrooms,
                minimum_nights = minimum_nights,
                zipcode = zipcode,
                host_neighbourhood = host_neighbourhood,
                property_type = property_type,
                room_type = room_type,
                optimal_price = abs( pred.json()[res][res] )

            )
        print('See ya space cowboy')