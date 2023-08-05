'''
Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?
This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint as shown above. You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJNeHD4p-540AR2Q0_ZjwmKJ8".

$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2453 characters
Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8
'''
import urllib.parse
import urllib.request
import urllib.error
import json
import ssl

base_url = "http://py4e-data.dr-chuck.net/json?"
api_key = 42

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#defining location func
def get_place_id(location):
    #completing url
    parms = dict()
    parms['address'] = location
    parms['key'] = api_key
    url = base_url + urllib.parse.urlencode(parms)
    print("Retrieving", url)

    #making the request and decoding it
    try:
        response = urllib.request.urlopen(url, context=ctx)
        data = response.read().decode()
        if len(data) < 1:
            print("Error: Empty response")
            return None
        
        json_data = json.loads(data)
        if 'results' in json_data and len(json_data['results']) > 0:
            place_id = json_data['results'][0]['place_id']
            return place_id
        else:
            print("Error: No results found in the JSON response")
    except Exception as e:
        print("Error:", e)

    return None
    


def main():
    #Entering the location
    location = input("Enter location: ")
    #Getting the id from the method
    place_id = get_place_id(location)
    
    if place_id:
        print("Place id", place_id)
    else:
        print("Place id not found.")


if __name__ == "__main__":
    main()