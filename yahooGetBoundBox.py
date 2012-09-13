#!/usr/bin/env python
'''
 Find the bounding box latitudes and longitudes of cities
 using the Yahoo! GeoPlanet and PlaceFinder API

 Input: locs.txt
        A file that contains the cities we are interested in
        with each city on a separate line.
        The Yahoo! GeoPlanet API we will be using
        to gather WOEIDs of cities supports many formats of inputs.

 Output: boundbox.txt
        A file containing the northeast and southwest latitude and
        longitude values for the bounding box of each city.
        Each city has its own line with the format:
        id    cityname    NElat    NElng    SWlat    SWlng
        
Written by Amy X Zhang
amy.xian.zhang@gmail.com
http://amyxzhang.wordpress.com
'''

import json
import urllib



'''
Get WOEIDs of cities.

Using Yahoo! GeoPlanet API
replace api_key with your API key from http://developer.yahoo.com/geo/geoplanet/
'''

api_key = 'dj0yJmk9VW9hUnJMTkN1djV4JmQ9WVdrOVdIVkNSMm93TXpZbWNHbzlNemsxTnpBeE5EWXkmcz1jb25zdW1lcnNlY3JldCZ4PTVm'

base = 'http://where.yahooapis.com/geocode?'

#read in city names
cities = []
nfile = open('locs.txt',"r")
lines = nfile.readlines()
for line in lines:
    line = line.strip()
    cities.append(line)

woeids = []

#uncomment to print WOEIDS to file
#file2 = open('woeids.txt',"w")
for loc in cities:
    first = 'location=' + loc + '&flags=J&appid='
    url = base + first + api_key
    result = json.load(urllib.urlopen(url))
    print result
    a = result['ResultSet']['Results'][0]['city']
    b = result['ResultSet']['Results'][0]['woeid']
    #file2.write(a + '\t')
    #file2.write(str(b) + '\n')
    woeids.append(b)
#file2.close()



'''
Get bounding box info given WOEIDs of cities and print to file.

Using Yahoo! PlaceFinder API
replace api_key2 with your API key from http://developer.yahoo.com/geo/placefinder/
'''

api_key2 = '57I4wiLV34EjVWNCYuOFTqGNMtPGfy0xgczCCNI8yS6J7RLauyMcH9X8sLLa_NzC'

base = 'http://where.yahooapis.com/v1/places'

ff = open('boundbox.txt','w')
for id in woeids:
    first = '.woeid(' + str(id) + ')?&format=json&appid='
    url = base + first + api_key2
    result = json.load(urllib.urlopen(url))

    print result
    
    name = result['places']['place'][0]['name']
    print name
    ff.write(name)
    #NorthEast point
    for item in result['places']['place'][0]['boundingBox']['northEast']:
        print item + ':' + str(result['places']['place'][0]['boundingBox']['northEast'][item])
        ff.write('\t' + str(result['places']['place'][0]['boundingBox']['northEast'][item]))
    #SouthWest point
    for item in result['places']['place'][0]['boundingBox']['southWest']:
        print item + ':' + str(result['places']['place'][0]['boundingBox']['southWest'][item])
        ff.write('\t' + str(result['places']['place'][0]['boundingBox']['southWest'][item]))
    ff.write('\n')
    
ff.close()