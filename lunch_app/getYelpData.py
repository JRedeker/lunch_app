from requests_oauthlib import OAuth1Session
import requests
import json
from pprint import pprint
#Yelp Authentication documentation [OAuth 1.0]: https://www.yelp.com/developers/documentation/v2/authentication

#Yelp Search API Doc: https://www.yelp.com/developers/documentation/v2/search_api

#import API Keys from external file
with open('config.json') as config_file: #config.json will need to exist in flask root, otherwise hardlinking may be necessary
    config = json.load(config_file)

OAuthAppKey = config['keys']['yelp']['OAuthAppKey']
OAuthAppSecret = config['keys']['yelp']['OAuthAppSecret']
OAuthUserKey = config['keys']['yelp']['OAuthUserKey']
OAuthUserSecret = config['keys']['yelp']['OAuthUserSecret']


##to be imported via browser/user feedback

#&ll=latitude,longitude
latitude = '42.846319099999995'
longitude = '-85.7139251'

searchTerm = 'chinese food' #&term=   #Search term If term isnt included we search everything.
radius = 1609*8 #&radius_filter=    #~1609 meters in 1 mile, Yelp API searches with meters, max value is 40000
resultsLimit = '1' #&limit=


#Start Session with OAuth Authentication
yelpAuth = OAuth1Session(OAuthAppKey,
		     client_secret=OAuthAppSecret,
		     resource_owner_key=OAuthUserKey,
		     resource_owner_secret=OAuthUserSecret)
#request URL
url='https://api.yelp.com/v2/search'

params = {'term': searchTerm,
	 'radius_filter': radius,
	 'limit': resultsLimit,
	 'll':latitude + ',' + longitude}

request = yelpAuth.get(url, params = params)

json = request.json()


name = json['businesses'][0]['name']
phone = json['businesses'][0]['display_phone']
street_address = json['businesses'][0]['location']['address']
city = json['businesses'][0]['location']['city']
state = json['businesses'][0]['location']['state_code']
postal_code = json['businesses'][0]['location']['postal_code']
image_url = json['businesses'][0]['image_url']

pprint(json)
#print(json.dump({'name': name , 'address': street_address, 'phone': phone, 'image_url': image_url})

#pprint(json)

''' example json
{u'businesses': [{u'categories': [[u'Chinese', u'chinese']],
                  u'display_phone': u'+1-616-257-3378',
                  u'distance': 4343.846490223262,
                  u'id': u'great-lakes-chinese-restaurant-wyoming',
                  u'image_url': u'http://s3-media3.fl.yelpcdn.com/bphoto/MWoYFVH-5j4ugq4cwTK74Q/ms.jpg',
                  u'is_claimed': True,
                  u'is_closed': False,
                  u'location': {u'address': [u'1851 44th St SW'],
                                u'city': u'Wyoming',
                                u'coordinate': {u'latitude': 42.8847149,
                                                u'longitude': -85.7098467},
                                u'country_code': u'US',
                                u'display_address': [u'1851 44th St SW',
                                                     u'Wyoming, MI 49519'],
                                u'geo_accuracy': 8.0,
                                u'postal_code': u'49519',
                                u'state_code': u'MI'},
                  u'menu_date_updated': 1442401427,
                  u'menu_provider': u'single_platform',
                  u'mobile_url': u'http://m.yelp.com/biz/great-lakes-chinese-restaurant-wyoming?utm_campaign=yelp_api&utm_medium=api_v2_search&utm_source=JA2vPxghMYi8UxfXKFGsxg',
                  u'name': u'Great Lakes Chinese Restaurant',
                  u'phone': u'6162573378',
                  u'rating': 4.0,
                  u'rating_img_url': u'http://s3-media4.fl.yelpcdn.com/assets/2/www/img/c2f3dd9799a5/ico/stars/v1/stars_4.png',
                  u'rating_img_url_large': u'http://s3-media2.fl.yelpcdn.com/assets/2/www/img/ccf2b76faa2c/ico/stars/v1/stars_large_4.png',
                  u'rating_img_url_small': u'http://s3-media4.fl.yelpcdn.com/assets/2/www/img/f62a5be2f902/ico/stars/v1/stars_small_4.png',
                  u'review_count': 28,
                  u'snippet_image_url': u'http://s3-media1.fl.yelpcdn.com/photo/lFl2H7L_VNbNA6ftfDnbpg/ms.jpg',
                  u'snippet_text': u'Decent food, the price is right (especially for their lunch buffet), but where this place really shines is its staff. This is hands-down the friendliest...',
                  u'url': u'http://www.yelp.com/biz/great-lakes-chinese-restaurant-wyoming?utm_campaign=yelp_api&utm_medium=api_v2_search&utm_source=JA2vPxghMYi8UxfXKFGsxg'}],
 u'region': {u'center': {u'latitude': 42.86581339999999,
                         u'longitude': -85.7122576},
             u'span': {u'latitude_delta': 0.042887460000002875,
                       u'longitude_delta': 0.003668500000003405}},
 u'total': 37}
'''