import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    #test
    print("\nTest")
    print(urllib.parse.parse_qs(url))
    print("\n-----------------------------------")

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode() #utf-8 outside to string inside
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data) # Trying to check for json into the string structure, if found, returning a py dict
    except:
        js = None


#checking if json to dict worked, and also if worked with the json conversion to dict, 
# if it's in the way we want, with Status key and value OK
    if not js or 'status' not in js or js['status'] != 'OK': 
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4)) # Prints the hole json requested


    # Prints out specific json tree chosen data, or better saying, the objects and their hierarchical objects too.
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)