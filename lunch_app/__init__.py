# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import Response
from requests_oauthlib import OAuth1Session
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index-mdl.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')

@app.route("/old")
def test():
    return render_template('index-new.html')


@app.route("/testajax", methods=['POST'])
def testajax():
    print "HELLOOOOOOOOOOOOOO"
    return Response("worked", mimetype='html/text')

@app.route("/api/1/getYelpData", methods=['GET, POST'])
def yelpData():
    #Yelp Authentication documentation [OAuth 1.0]: https://www.yelp.com/developers/documentation/v2/authentication

    #Yelp Search API Doc: https://www.yelp.com/developers/documentation/v2/search_api

    #import API Keys from external file
    try:
        with open('/var/www/lunch_app/lunch_app/config.json') as config_file: #config.json will need to exist in flask root, otherwise hardlinking may be necessary
            config = json.load(config_file)
    except:
        return render_template('generic_error.html')



    OAuthAppKey = config['keys']['yelp']['OAuthAppKey']
    OAuthAppSecret = config['keys']['yelp']['OAuthAppSecret']
    OAuthUserKey = config['keys']['yelp']['OAuthUserKey']
    OAuthUserSecret = config['keys']['yelp']['OAuthUserSecret']


    ##to be imported via browser/user feedback

    #&ll=latitude,longitude
    latitude = '42.846319099999995'
    longitude = '-85.7139251'

    searchTerm = 'chinese food' #&term=   #Search term If term isnt included we search everything.
    #radius = 1609*8 #&radius_filter=    #~1609 meters in 1 mile, Yelp API searches with meters, max value is 40000
    resultsLimit = '1' #&limit=

    #latitude = request.form['latitude']
    #longitude = request.form['longitude']
    #searchTerm = request.form['options'] #&term=   #Search term If term isnt included we search everything.
    radius = 1609 * request.form['distance'] #&radius_filter=    #~1609 meters in 1 mile, Yelp API searches with meters, max value is 40000
    #resultsLimit = request.form['resultsLimit'] #&limit=

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

    requestJSON = request.json()


    name = requestJSON['businesses'][0]['name']
    phone = requestJSON['businesses'][0]['display_phone']
    street_address = requestJSON['businesses'][0]['location']['address']
    city = requestJSON['businesses'][0]['location']['city']
    state = requestJSON['businesses'][0]['location']['state_code']
    postal_code = requestJSON['businesses'][0]['location']['postal_code']
    image_url = requestJSON['businesses'][0]['image_url']

    try:
        standardJSON = { 'name' : name,
                'street address' : street_address,
                'city' : city,
                'state' : state,
                'postal_code' : postal_code,
                'image_url': image_url
                }
        return Response(json.dumps(standardJSON), mimetype='application/json')
    except:
        return render_template('generic_error.html')

@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
