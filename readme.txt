 Find the bounding box coordinates that encompass a city
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

 This code could potentially also be used, with minor tweaking, to 
 find bounding box values for entities other than cities, depending 
 on what else is available on Yahoo! PlaceFinder, such as counties 
 and neighborhoods.


Yahoo! GeoPlanet
http://developer.yahoo.com/geo/geoplanet/

Yahoo! PlaceFinder
http://developer.yahoo.com/geo/placefinder/
        
Written by Amy X Zhang
amy.xian.zhang@gmail.com
http://amyxzhang.wordpress.com