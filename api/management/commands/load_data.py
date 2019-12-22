from django.core.management.base import BaseCommand, CommandError
import pytz
import csv
from api.models import Airbnb
import random
import datetime



class Command(BaseCommand):
    help = 'Overwrites data in database'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs=1, type=str)

    def handle(self, *args, **options):
        
        Airbnb.objects.all().delete()
               
        with open(options['path'][0]) as csv_file:
            
            csv_reader = csv.reader(csv_file, delimiter=',')
            print("loading data from: ", options['path'][0])
            line_count = 0
            
            for row in csv_reader:
                if line_count != 0:
                    
                    Airbnb.objects.create(
                        id=row[0],
                        listing_url=row[1],
                        scrape_id=row[2],
                        last_scraped=row[3],
                        name=row[4],
                        summary=row[5],
                        space=row[6],
                        description=row[7],
                        experiences_offered=row[8],
                        neighborhood_overview=row[9],
                        notes=row[10],
                        transit=row[11],
                        access=row[12],
                        interaction=row[13],
                        house_rules=row[14],
                        thumbnail_url=row[15],
                        medium_url=row[16],
                        picture_url=row[17],
                        xl_picture_url=row[18],
                        host_id=row[19],
                        host_url=row[20],
                        host_name=row[21],
                        host_since=row[22],
                        host_location=row[23],
                        host_about=row[24],
                        host_response_time=row[25],
                        host_response_rate=row[26],
                        host_acceptance_rate=row[27],
                        host_is_superhost=row[28],
                        host_thumbnail_url=row[29],
                        host_picture_url=row[30],
                        host_neighbourhood=row[31],
                        host_listings_count=row[32],
                        host_total_listings_count=row[33],
                        host_verifications=row[34],
                        host_has_profile_pic=row[35],
                        host_identity_verified=row[36],
                        street=row[37],
                        neighbourhood=row[38],
                        neighbourhood_cleansed=row[39],
                        neighbourhood_group_cleansed=row[40],
                        city=row[41],
                        state=row[42],
                        zipcode=row[43],
                        market=row[44],
                        smart_location=row[45],
                        country_code=row[46],
                        country=row[47],
                        latitude=row[48],
                        longitude=row[49],
                        is_location_exact=row[50],
                        property_type=row[51],
                        room_type=row[52],
                        accommodates=row[53],
                        bathrooms=row[54],
                        bedrooms=row[55],
                        beds=row[56],
                        bed_type=row[57],
                        amenities=row[58],
                        square_feet=row[59],
                        price=row[60],
                        weekly_price=row[61],
                        monthly_price=row[62],
                        security_deposit=row[63],
                        cleaning_fee=row[64],
                        guests_included=row[65],
                        extra_people=row[66],
                        minimum_nights=row[67],
                        maximum_nights=row[68],
                        minimum_minimum_nights=row[69],
                        maximum_minimum_nights=row[70],
                        minimum_maximum_nights=row[71],
                        maximum_maximum_nights=row[72],
                        minimum_nights_avg_ntm=row[73],
                        maximum_nights_avg_ntm=row[74],
                        calendar_updated=row[75],
                        has_availability=row[76],
                        availability_30=row[77],
                        availability_60=row[78],
                        availability_90=row[79],
                        availability_365=row[80],
                        calendar_last_scraped=row[81],
                        number_of_reviews=row[82],
                        number_of_reviews_ltm=row[83],
                        first_review=row[84],
                        last_review=row[85],
                        review_scores_rating=row[86],
                        review_scores_accuracy=row[87],
                        review_scores_cleanliness=row[88],
                        review_scores_checkin=row[89],
                        review_scores_communication=row[90],
                        review_scores_location=row[91],
                        review_scores_value=row[92],
                        requires_license=row[93],
                        license=row[94],
                        jurisdiction_names=row[95],
                        instant_bookable=row[96],
                        is_business_travel_ready=row[97],
                        cancellation_policy=row[98],
                        require_guest_profile_picture=row[99],
                        require_guest_phone_verification=row[100],
                        calculated_host_listings_count=row[101],
                        calculated_host_listings_count_entire_homes=row[102],
                        calculated_host_listings_count_private_rooms=row[103],
                        calculated_host_listings_count_shared_rooms=row[104],
                        reviews_per_month=row[105],
                        )
                        
                line_count += 1