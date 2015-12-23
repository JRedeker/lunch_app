# -*- coding: utf-8 -*-


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
